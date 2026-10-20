package com.asadullahnotes.mcq

import android.app.Activity
import android.app.AlertDialog
import android.content.res.Configuration
import android.graphics.Color
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.SystemClock
import android.view.View
import android.view.ViewGroup
import android.view.WindowInsets
import android.view.WindowInsetsController
import android.webkit.JsPromptResult
import android.webkit.JsResult
import android.webkit.RenderProcessGoneDetail
import android.webkit.WebChromeClient
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.FrameLayout
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.Toast
import androidx.webkit.WebMessageCompat
import androidx.webkit.WebSettingsCompat
import androidx.webkit.WebViewAssetLoader
import androidx.webkit.WebViewCompat
import androidx.webkit.WebViewFeature

/**
 * Asadullah Notes - thin native shell around the bundled (offline) web app.
 *
 * - Content is served from the APK assets through https://appassets.androidplatform.net (WebViewAssetLoader), so localStorage works
 *   normally, nothing is read from the file system and no network permission is needed.
 * - Navigation is restricted to that origin; everything else is blocked.
 */
class MainActivity : Activity() {

    private lateinit var webView: WebView
    private lateinit var splash: View
    private lateinit var topBar: View
    private lateinit var bottomBar: View
    private lateinit var assetLoader: WebViewAssetLoader
    private var lastBackPress = 0L
    private var night = false
    private var pageShown = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        assetLoader = WebViewAssetLoader.Builder()
            .setDomain(HOST)
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .build()
        buildUi()
        applyBars(false)
        if (savedInstanceState != null && webView.restoreState(savedInstanceState) != null) {
            // history restored; page itself is re-created by the WebView
        } else {
            webView.loadUrl(START_URL)
        }
    }

    // ---------------------------------------------------------------- UI

    private fun buildUi() {
        val column = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(getColor(R.color.brand))
        }
        topBar = View(this).apply { setBackgroundColor(getColor(R.color.brand)) }
        bottomBar = View(this).apply { setBackgroundColor(getColor(R.color.nav_day)) }
        val content = FrameLayout(this).apply { setBackgroundColor(getColor(R.color.brand)) }

        webView = WebView(this)
        configureWebView(webView)
        webView.visibility = View.INVISIBLE            // revealed by onPageFinished: no blank/white flash
        content.addView(webView, ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT)

        splash = FrameLayout(this).apply {
            setBackgroundColor(getColor(R.color.brand))
            addView(ImageView(context).apply { setImageResource(R.drawable.ic_logo) },
                FrameLayout.LayoutParams(dp(112), dp(112), android.view.Gravity.CENTER))
        }
        content.addView(splash, ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT)

        column.addView(topBar, LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0))
        column.addView(content, LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0, 1f))
        column.addView(bottomBar, LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0))
        setContentView(column)

        // Android 15+ always draws edge-to-edge: reserve the system-bar (and keyboard) areas ourselves.
        // Older versions keep the normal opaque system bars, so no extra space is needed there.
        if (Build.VERSION.SDK_INT >= 35) {
            column.setOnApplyWindowInsetsListener { _, insets ->
                val bars = insets.getInsets(WindowInsets.Type.systemBars() or WindowInsets.Type.displayCutout())
                val ime = insets.getInsets(WindowInsets.Type.ime())
                topBar.layoutParams = topBar.layoutParams.apply { height = bars.top }
                bottomBar.layoutParams = bottomBar.layoutParams.apply { height = maxOf(bars.bottom, ime.bottom) }
                column.setPadding(bars.left, 0, bars.right, 0)
                WindowInsets.CONSUMED
            }
        }
    }

    private fun dp(v: Int) = (v * resources.displayMetrics.density + 0.5f).toInt()

    /** Status/navigation bar colours follow the page's day/night theme. */
    private fun applyBars(nightMode: Boolean) {
        night = nightMode
        val top = getColor(if (nightMode) R.color.brand_night else R.color.brand)
        val nav = getColor(if (nightMode) R.color.nav_night else R.color.nav_day)
        topBar.setBackgroundColor(top)
        bottomBar.setBackgroundColor(nav)
        @Suppress("DEPRECATION")
        if (Build.VERSION.SDK_INT < 35) {
            window.statusBarColor = top
            window.navigationBarColor = nav
        }
        // status-bar icons: always light (bar is dark indigo); navigation icons: dark on the light bar, light on the dark bar
        if (Build.VERSION.SDK_INT >= 30) {
            window.insetsController?.apply {
                setSystemBarsAppearance(0, WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS)
                setSystemBarsAppearance(
                    if (nightMode) 0 else WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                    WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS
                )
            }
        } else {
            @Suppress("DEPRECATION")
            var flags = window.decorView.systemUiVisibility and View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR.inv()
            @Suppress("DEPRECATION")
            if (Build.VERSION.SDK_INT >= 26) {
                flags = if (nightMode) flags and View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR.inv()
                else flags or View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
            }
            @Suppress("DEPRECATION")
            window.decorView.systemUiVisibility = flags
        }
    }

    // ---------------------------------------------------------------- WebView

    private fun configureWebView(wv: WebView) {
        wv.setBackgroundColor(Color.TRANSPARENT)
        wv.overScrollMode = View.OVER_SCROLL_NEVER
        wv.isVerticalScrollBarEnabled = false
        wv.isHorizontalScrollBarEnabled = false
        wv.isLongClickable = false
        wv.setOnLongClickListener { true }              // no text-selection popup while tapping options
        wv.isHapticFeedbackEnabled = false

        wv.settings.apply {
            javaScriptEnabled = true                      // the app is JavaScript
            domStorageEnabled = true                      // localStorage: best scores, streak, theme, name
            @Suppress("DEPRECATION")
            databaseEnabled = false
            allowFileAccess = false
            allowContentAccess = false
            @Suppress("DEPRECATION")
            allowFileAccessFromFileURLs = false
            @Suppress("DEPRECATION")
            allowUniversalAccessFromFileURLs = false
            setSupportMultipleWindows(false)
            javaScriptCanOpenWindowsAutomatically = false
            setSupportZoom(false)
            builtInZoomControls = false
            displayZoomControls = false
            textZoom = 100                                // keep the designed text sizes whatever the system font scale is
            mixedContentMode = WebSettings.MIXED_CONTENT_NEVER_ALLOW
            mediaPlaybackRequiresUserGesture = true
            cacheMode = WebSettings.LOAD_DEFAULT
            setGeolocationEnabled(false)
            if (Build.VERSION.SDK_INT >= 26) safeBrowsingEnabled = false   // only local content is ever loaded
        }
        // the page has its own day/night theme: never let the system "force dark" invert it
        if (WebViewFeature.isFeatureSupported(WebViewFeature.ALGORITHMIC_DARKENING)) {
            WebSettingsCompat.setAlgorithmicDarkeningAllowed(wv.settings, false)
        } else if (Build.VERSION.SDK_INT in 29..32) {
            @Suppress("DEPRECATION")
            WebSettingsCompat.setForceDark(wv.settings, WebSettingsCompat.FORCE_DARK_OFF)
        }
        WebView.setWebContentsDebuggingEnabled(false)

        // theme bridge: only our own origin may talk to the app, and the only message is "night" / "day"
        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {
            WebViewCompat.addWebMessageListener(wv, "AsadApp", setOf("https://$HOST")) { _, message: WebMessageCompat, _, _, _ ->
                val m = message.data
                if (m == "night" || m == "day") runOnUiThread { applyBars(m == "night") }
            }
        }

        wv.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(view: WebView, request: WebResourceRequest): WebResourceResponse? =
                assetLoader.shouldInterceptRequest(request.url)

            override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean =
                !isAppUrl(request.url)                    // anything outside the app is blocked

            override fun onPageFinished(view: WebView, url: String) {
                if (!pageShown) {
                    pageShown = true
                    view.visibility = View.VISIBLE
                    splash.animate().alpha(0f).setDuration(120).withEndAction { splash.visibility = View.GONE }.start()
                }
            }

            override fun onReceivedError(view: WebView, request: WebResourceRequest, error: WebResourceError) {
                if (request.isForMainFrame) showErrorPage(view, request.url)
            }

            override fun onReceivedHttpError(view: WebView, request: WebResourceRequest, errorResponse: WebResourceResponse) {
                if (request.isForMainFrame) showErrorPage(view, request.url)
            }

            override fun onRenderProcessGone(view: WebView, detail: RenderProcessGoneDetail): Boolean {
                // the WebView process died (usually low memory): rebuild the screen instead of crashing
                recreate()
                return true
            }
        }

        // JavaScript confirm()/alert() are used by the app (leave test, submit): WebView needs real dialogs for them
        wv.webChromeClient = object : WebChromeClient() {
            override fun onJsAlert(view: WebView, url: String?, message: String?, result: JsResult): Boolean {
                AlertDialog.Builder(this@MainActivity).setMessage(message)
                    .setPositiveButton(R.string.ok) { _, _ -> result.confirm() }
                    .setOnCancelListener { result.cancel() }.show()
                return true
            }

            override fun onJsConfirm(view: WebView, url: String?, message: String?, result: JsResult): Boolean {
                AlertDialog.Builder(this@MainActivity).setMessage(message)
                    .setPositiveButton(R.string.ok) { _, _ -> result.confirm() }
                    .setNegativeButton(R.string.cancel) { _, _ -> result.cancel() }
                    .setOnCancelListener { result.cancel() }.show()
                return true
            }

            override fun onJsPrompt(view: WebView, url: String?, message: String?, defaultValue: String?, result: JsPromptResult): Boolean {
                result.cancel(); return true
            }
        }
    }

    private fun isAppUrl(u: Uri) = u.scheme == "https" && u.host == HOST

    private fun showErrorPage(view: WebView, failed: Uri) {
        if (failed.path?.endsWith("/error.html") == true) return    // never loop
        view.loadUrl(ERROR_URL)
    }

    // ---------------------------------------------------------------- lifecycle / navigation

    @Deprecated("Deprecated in Java")
    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()                              // the page handles it (asks before leaving a running test)
            return
        }
        val now = SystemClock.elapsedRealtime()
        if (now - lastBackPress < 2000) {
            @Suppress("DEPRECATION")
            super.onBackPressed()
        } else {
            lastBackPress = now
            Toast.makeText(this, R.string.press_back_again, Toast.LENGTH_SHORT).show()
        }
    }

    override fun onPause() {
        webView.onPause()
        webView.pauseTimers()                             // no timers/animations while in the background (no duplicates on resume)
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        webView.resumeTimers()
        webView.onResume()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        webView.saveState(outState)
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)           // declared in the manifest: the page is not recreated on rotation/font change
    }

    override fun onDestroy() {
        (webView.parent as? ViewGroup)?.removeView(webView)
        webView.stopLoading()
        webView.destroy()
        super.onDestroy()
    }

    companion object {
        private const val HOST = "appassets.androidplatform.net"
        private const val START_URL = "https://$HOST/assets/www/index.html"
        private const val ERROR_URL = "https://$HOST/assets/www/error.html"
    }
}
