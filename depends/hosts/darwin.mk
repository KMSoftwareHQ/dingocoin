OSX_MIN_VERSION=11.0
OSX_SDK=$(shell xcrun --show-sdk-path)

darwin_CC=clang -target $(host) -mmacosx-version-min=$(OSX_MIN_VERSION)
darwin_CXX=clang++ -target $(host) -mmacosx-version-min=$(OSX_MIN_VERSION) -stdlib=libc++

darwin_CFLAGS=-pipe
darwin_CXXFLAGS=$(darwin_CFLAGS)
darwin_CPPFLAGS=-isysroot $(OSX_SDK)
darwin_LDFLAGS=-isysroot $(OSX_SDK)

darwin_release_CFLAGS=-O2
darwin_release_CXXFLAGS=$(darwin_release_CFLAGS)

darwin_debug_CFLAGS=-O1
darwin_debug_CXXFLAGS=$(darwin_debug_CFLAGS)

darwin_native_toolchain=
