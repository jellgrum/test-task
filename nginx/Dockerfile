FROM nginx:1.28.3-alpine

# Fix CVE-2026-33416: libpng arbitrary code execution (use-after-free)
# Upgrade libpng to a patched version
RUN apk upgrade --no-cache libpng
