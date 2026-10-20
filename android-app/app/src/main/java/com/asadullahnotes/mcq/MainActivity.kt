package com.asadullahnotes.mcq

import android.app.Activity
import android.app.AlertDialog
import android.content.res.Configuration
import android.graphics.Color
import android.widget.TextView
import android.util.TypedValue
import android.graphics.Typeface
import android.graphics.drawable.GradientDrawable
import android.graphics.drawable.ColorDrawable
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
    private var topColor = 0   // 0 = not reported yet (brand colour)
    private var topInsetPx = 0 // status-bar height on Android 15+, where the page is drawn behind it
    private var pageShown = false
    private var crashCount = 0
    private var openDialog: AlertDialog? = null
    private var pendingResult: JsResult? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        assetLoader = WebViewAssetLoader.Builder()
            .setDomain(HOST)
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .build()
        buildUi()
        night = savedInstanceState?.getBoolean("night") ?: false
        topColor = savedInstanceState?.getInt("top") ?: 0
        applyBars(night)
        window.decorView.post { applyBars(night) }   // the insets controller is not always ready inside onCreate (Android 11)
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
                // the page itself is drawn behind the status bar (so its background reaches the very top);
                // the page gets the bar height as the CSS variable --sat and pads its header with it
                topInsetPx = bars.top
                topBar.layoutParams = topBar.layoutParams.apply { height = 0 }
                applyInsetToPage()
                bottomBar.layoutParams = bottomBar.layoutParams.apply { height = maxOf(bars.bottom, ime.bottom) }
                column.setPadding(bars.left, 0, bars.right, 0)
                WindowInsets.CONSUMED
            }
        }
    }

    /** Tell the page how tall the status bar is (CSS pixels), so fixed/sticky top elements start below it. */
    private fun applyInsetToPage() {
        if (!::webView.isInitialized) return
        val css = topInsetPx / resources.displayMetrics.density
        webView.evaluateJavascript(
            "document.documentElement.style.setProperty('--sat','" + String.format(java.util.Locale.US, "%.1f", css) + "px')", null)
    }

    private fun dp(v: Int) = (v * resources.displayMetrics.density + 0.5f).toInt()

    /** Status/navigation bar colours follow the page's day/night theme. */
    private fun applyBars(nightMode: Boolean) {
        night = nightMode
        val top = if (topColor != 0) topColor else getColor(if (nightMode) R.color.brand_night else R.color.brand)
        val nav = getColor(if (nightMode) R.color.nav_night else R.color.nav_day)
        topBar.setBackgroundColor(top)
        bottomBar.setBackgroundColor(nav)
        @Suppress("DEPRECATION")
        if (Build.VERSION.SDK_INT < 35) {
            window.statusBarColor = top
            window.navigationBarColor = nav
        }
        // status-bar icons: dark icons on a light bar, light icons on a dark bar; navigation icons follow the day/night theme
        val lightTop = isLight(top)
        if (Build.VERSION.SDK_INT >= 30) {
            window.insetsController?.apply {
                setSystemBarsAppearance(
                    if (lightTop) WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS else 0,
                    WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                )
                setSystemBarsAppearance(
                    if (nightMode) 0 else WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                    WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS
                )
            }
        } else {
            @Suppress("DEPRECATION")
            var flags = window.decorView.systemUiVisibility
            @Suppress("DEPRECATION")
            flags = if (lightTop) flags or View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR else flags and View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR.inv()
            @Suppress("DEPRECATION")
            if (Build.VERSION.SDK_INT >= 26) {
                flags = if (nightMode) flags and View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR.inv()
                else flags or View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
            }
            @Suppress("DEPRECATION")
            window.decorView.systemUiVisibility = flags
        }
    }

    private fun isLight(c: Int): Boolean =
        (0.299 * Color.red(c) + 0.587 * Color.green(c) + 0.114 * Color.blue(c)) > 160

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

        // theme bridge: only our own origin may talk to the app, and messages are "night" / "day" / "top:#rrggbb" (status-bar colour)
        if (WebViewFeature.isFeatureSupported(WebViewFeature.WEB_MESSAGE_LISTENER)) {
            WebViewCompat.addWebMessageListener(wv, "AsadApp", setOf("https://$HOST")) { _, message: WebMessageCompat, _, _, _ ->
                val m = message.data
                if (m == "night" || m == "day") runOnUiThread { applyBars(m == "night") }
                else if (m != null && TOP_RE.matches(m)) runOnUiThread { topColor = Color.parseColor(m.substring(4)); applyBars(night) }
            }
        }

        wv.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(view: WebView, request: WebResourceRequest): WebResourceResponse? =
                assetLoader.shouldInterceptRequest(request.url)

            override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean =
                !isAppUrl(request.url)                    // anything outside the app is blocked

            override fun onPageCommitVisible(view: WebView, url: String) { applyInsetToPage() }

            override fun onPageFinished(view: WebView, url: String) {
                applyInsetToPage()
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
                if (++crashCount > 2) { finish(); return true }   // never loop forever if the page itself kills the renderer
                recreate()
                return true
            }
        }

        // JavaScript confirm()/alert() are used by the app (leave test, submit): WebView needs real dialogs for them
        wv.webChromeClient = object : WebChromeClient() {
            override fun onJsAlert(view: WebView, url: String?, message: String?, result: JsResult): Boolean {
                showAppDialog(message ?: "", false, result); return true
            }

            override fun onJsConfirm(view: WebView, url: String?, message: String?, result: JsResult): Boolean {
                showAppDialog(message ?: "", true, result); return true
            }

            override fun onJsBeforeUnload(view: WebView, url: String?, message: String?, result: JsResult): Boolean { result.confirm(); return true }

            override fun onJsPrompt(view: WebView, url: String?, message: String?, defaultValue: String?, result: JsPromptResult): Boolean {
                result.cancel(); return true
            }
        }
    }

    /** App-styled replacement for the plain system dialog used by the page's confirm()/alert(). */
    private fun showAppDialog(message: String, confirmType: Boolean, result: JsResult) {
        if (isFinishing || isDestroyed) { result.cancel(); return }
        val leave = message.contains("Leave this test", true) || message.contains("chhor dein", true)
        val logout = message.contains("Log out", true)
        val title: String; val body: String; val yes: String; val no: String; val icon: String
        val accent: Int
        when {
            leave -> { title = "Leave this test?"; body = "Your progress in this test will be lost."; yes = "Leave"; no = "Stay"; icon = "!"; accent = Color.parseColor("#E11D48") }
            logout -> { title = "Log out?"; body = "Do you want to log out of Asadullah Notes?"; yes = "Log out"; no = "Cancel"; icon = "\u21AA"; accent = Color.parseColor("#E11D48") }
            else -> { title = "Asadullah Notes"; body = message; yes = "OK"; no = "Cancel"; icon = "i"; accent = Color.parseColor("#4F46E5") }
        }
        val dark = night
        val card = if (dark) Color.parseColor("#17114A") else Color.WHITE
        val ink = if (dark) Color.parseColor("#F3EFFF") else Color.parseColor("#0F172A")
        val sub = if (dark) Color.parseColor("#BDB3E6") else Color.parseColor("#475569")
        val indigo = Color.parseColor("#4F46E5")
        fun pill(fill: Int, stroke: Int = 0) = GradientDrawable().apply {
            cornerRadius = dp(14).toFloat(); setColor(fill); if (stroke != 0) setStroke(dp(1), stroke)
        }
        fun tv(text: String, sp: Float, color: Int, bold: Boolean) = TextView(this).apply {
            this.text = text; setTextSize(TypedValue.COMPLEX_UNIT_SP, sp); setTextColor(color)
            if (bold) typeface = Typeface.DEFAULT_BOLD; gravity = android.view.Gravity.CENTER
        }
        val panel = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(dp(22), dp(26), dp(22), dp(20))
            background = GradientDrawable().apply {
                cornerRadius = dp(26).toFloat(); setColor(card)
                if (dark) setStroke(dp(1), Color.parseColor("#33FFFFFF"))
            }
            elevation = dp(8).toFloat()
        }
        val badge = tv(icon, 30f, accent, true).apply {
            background = GradientDrawable().apply { shape = GradientDrawable.OVAL; setColor((accent and 0x00FFFFFF) or 0x22000000) }
        }
        panel.addView(badge, LinearLayout.LayoutParams(dp(64), dp(64)).apply { gravity = android.view.Gravity.CENTER_HORIZONTAL; bottomMargin = dp(14) })
        panel.addView(tv(title, 20f, ink, true), LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = dp(8) })
        panel.addView(tv(body, 15f, sub, false).apply { setLineSpacing(0f, 1.15f) }, LinearLayout.LayoutParams(-1, -2).apply { bottomMargin = dp(22) })
        val row = LinearLayout(this).apply { orientation = LinearLayout.HORIZONTAL }
        val dialog = AlertDialog.Builder(this).create()
        openDialog = dialog; pendingResult = result
        var answered = false
        fun finish(ok: Boolean) { if (answered) return; answered = true; pendingResult = null; if (ok) result.confirm() else result.cancel(); dialog.dismiss() }
        if (confirmType) {
            val stay = tv(no, 16f, indigo, true).apply { background = pill(Color.TRANSPARENT, indigo); setOnClickListener { finish(false) } }
            row.addView(stay, LinearLayout.LayoutParams(0, dp(48), 1f).apply { rightMargin = dp(6) })
        }
        val go = tv(if (confirmType) yes else "OK", 16f, Color.WHITE, true).apply {
            background = pill(if (confirmType) accent else indigo); setOnClickListener { finish(true) }
        }
        row.addView(go, LinearLayout.LayoutParams(0, dp(48), 1f).apply { if (confirmType) leftMargin = dp(6) })
        panel.addView(row, LinearLayout.LayoutParams(-1, -2))
        val holder = FrameLayout(this).apply { setPadding(dp(22), 0, dp(22), 0); addView(panel, FrameLayout.LayoutParams(-1, -2)) }
        dialog.setView(holder)
        dialog.setOnCancelListener { if (!answered) { answered = true; pendingResult = null; result.cancel() } }
        dialog.show()
        dialog.window?.apply {
            setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
            setDimAmount(0.55f)
            setLayout(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT)
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
        outState.putBoolean("night", night); outState.putInt("top", topColor)
        webView.saveState(outState)
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)           // declared in the manifest: the page is not recreated on rotation/font change
    }

    override fun onDestroy() {
        try { pendingResult?.cancel() } catch (e: Exception) {}
        pendingResult = null
        try { openDialog?.dismiss() } catch (e: Exception) {}
        openDialog = null
        (webView.parent as? ViewGroup)?.removeView(webView)
        webView.stopLoading()
        webView.destroy()
        super.onDestroy()
    }

    companion object {
        private const val HOST = "appassets.androidplatform.net"
        private const val START_URL = "https://$HOST/assets/www/index.html"
        private const val ERROR_URL = "https://$HOST/assets/www/error.html"
        private val TOP_RE = Regex("^top:#[0-9a-fA-F]{6}$")
    }
}
