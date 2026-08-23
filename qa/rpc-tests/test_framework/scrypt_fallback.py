#!/usr/bin/env python3
# Copyright (c) 2026 The Dingocoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Pure-Python fallback for the ltc_scrypt C extension.

qa/pull-tester/install-deps.sh fetches ltc_scrypt from
github.com/dingocoin/ltc-scrypt, which no longer exists (404), and the
ltc_scrypt 1.0 release on PyPI is Python 2 only -- it fails to compile
against Python 3 headers because it references PyStringObject. Without a
working ltc_scrypt, importing test_framework.mininode raises ImportError and
every functional test that pulls it in fails before it starts.

Litecoin-style scrypt proof-of-work is scrypt(N=1024, r=1, p=1, dklen=32)
over the 80-byte block header, used as both password and salt. hashlib
exposes exactly that on Python 3.6+ when linked against OpenSSL 1.1+, so no
external module is needed. This is slower than the C extension and is only
used when the extension is absent.
"""
import hashlib

# N * r * 128 = 1024 * 1 * 128 = 128 KiB of scratchpad; give OpenSSL headroom.
_MAXMEM = 1024 * 1024


def getPoWHash(data):
    """Return the 32-byte scrypt PoW hash of a block header."""
    return hashlib.scrypt(data, salt=data, n=1024, r=1, p=1, dklen=32,
                          maxmem=_MAXMEM)
