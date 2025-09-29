[app]
title = Ιστορία Γ Δημοτικού
package.name = historiagrade3
package.domain = gr.education

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy==2.1.0

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 23b

presplash.filename = presplash.png
