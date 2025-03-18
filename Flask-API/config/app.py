# Configuration file for the Flask app
APP_HOST = "0.0.0.0"
APP_PORT = 5005

# Configuration for debugging
# Jika ingin menjalankan Flask dalam mode debug, set DEBUG_MODE = True
# Jika ingin menjalankan Flask dalam mode production, set DEBUG_MODE = False
# Karena perbedaan cara menjalankan server, maka perlu diperhatikan
APP_DEBUG = False

# App Version
# Please update this version number every time you deploy a new version of the app
# This version number will be used for monitoring purposes
# Note: do not use the same version number for different deployments (for tracking purposes)
APP_VERSION = "1.1.7"
