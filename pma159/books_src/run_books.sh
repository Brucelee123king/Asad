#!/bin/bash
cd /home/user/Asad/pma159/books_src
[ -f ../books/psych/meta.json ] || python3 make_book.py psych "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/221.pdf" >> books_run.log 2>&1
[ -f ../books/khokhar/meta.json ] || python3 make_book.py khokhar "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/114.pdf" >> books_run.log 2>&1
[ -f ../books/noor/meta.json ] || python3 make_book.py noor "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/196.pdf" >> books_run.log 2>&1
[ -f ../books/pg1000/meta.json ] || python3 make_book.py pg1000 "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/228.pdf" >> books_run.log 2>&1
[ -f ../books/nv155/meta.json ] || python3 make_book.py nv155 "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/072.pdf" >> books_run.log 2>&1
[ -f ../books/vnv/meta.json ] || python3 make_book.py vnv "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/124.pdf" >> books_run.log 2>&1
[ -f ../books/issbbk/meta.json ] || python3 make_book.py issbbk "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/193.pdf" >> books_run.log 2>&1
[ -f ../books/gk3000/meta.json ] || python3 make_book.py gk3000 "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/062.pdf" >> books_run.log 2>&1
[ -f ../books/pafbook/meta.json ] || python3 make_book.py pafbook "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/000.pdf" >> books_run.log 2>&1
[ -f ../books/dogariq/meta.json ] || python3 make_book.py dogariq "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/078.pdf" >> books_run.log 2>&1
[ -f ../books/nvall/meta.json ] || python3 make_book.py nvall "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/111.pdf" >> books_run.log 2>&1
[ -f ../books/pafint/meta.json ] || python3 make_book.py pafint "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/028.pdf" >> books_run.log 2>&1
[ -f ../books/mech/meta.json ] || python3 make_book.py mech "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv2/dl/105.pdf" >> books_run.log 2>&1
[ -f ../books/nviq/meta.json ] || python3 make_book.py nviq "/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/intv/dl/095.pdf" >> books_run.log 2>&1
