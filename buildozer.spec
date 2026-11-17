[app]

# (str) Title of your application
title = Mi Lista de Compras

# (str) Package name
package.name = listadecompras

# (str) Package domain (needed for android packaging)
package.domain = org.compras

# (str) Version of your application
version = 0.1

# (str) Source directory where your source files are located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,urllib3,idna,certifi,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) android build tools version
android.build_tools_version = 31.0.0

# (list) Supported architectures
android.archs = arm64-v8a

# (str) python-for-android branch
p4a.branch = master
