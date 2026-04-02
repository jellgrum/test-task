FROM nginx:1.28.3-alpine

# Fix CVE-2026-33416: libpng arbitrary code execution (use-after-free)
# Upgrade  to a patched version
# Fix CVE-2026-22184: zlib arbitrary code execution via buffer overflow in untgz utility
# Upgrade libpng and zlib to a patched version (1.3.2-r0)
RUN apk upgrade --no-cache libpng zlib
