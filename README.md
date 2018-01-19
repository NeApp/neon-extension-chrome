# Neon Extension for Chrome
[![](https://img.shields.io/travis/NeApp/neon-extension-chrome.svg)](https://travis-ci.org/NeApp/neon-extension-chrome) ![](https://img.shields.io/github/license/NeApp/neon-extension-chrome.svg)

### Issues

Issues can be reported in the [neon-extension](https://github.com/NeApp/neon-extension) repository.

**Please include the following details:**

 - Browser Version
 - Extension Version
 - Operating System

## Modules

| Module                                                                                              | Status                                                                                                                                              | Coverage                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [neon-extension-core](https://github.com/NeApp/neon-extension-core)                                 | [![](https://img.shields.io/travis/NeApp/neon-extension-core.svg)](https://travis-ci.org/NeApp/neon-extension-core)                                 | [![](https://img.shields.io/coveralls/github/NeApp/neon-extension-core/master.svg)](https://coveralls.io/github/NeApp/neon-extension-core)           |
| [neon-extension-framework](https://github.com/NeApp/neon-extension-framework)                       | [![](https://img.shields.io/travis/NeApp/neon-extension-framework.svg)](https://travis-ci.org/NeApp/neon-extension-framework)                       | [![](https://img.shields.io/coveralls/github/NeApp/neon-extension-framework/master.svg)](https://coveralls.io/github/NeApp/neon-extension-framework) |
| [neon-extension-browser-base](https://github.com/NeApp/neon-extension-browser-base)                 | [![](https://img.shields.io/travis/NeApp/neon-extension-browser-base.svg)](https://travis-ci.org/NeApp/neon-extension-browser-base)                 |  |
| [neon-extension-browser-chrome](https://github.com/NeApp/neon-extension-browser-chrome)             | [![](https://img.shields.io/travis/NeApp/neon-extension-browser-chrome.svg)](https://travis-ci.org/NeApp/neon-extension-browser-chrome)             |  |
| [neon-extension-browser-webextension](https://github.com/NeApp/neon-extension-browser-webextension) | [![](https://img.shields.io/travis/NeApp/neon-extension-browser-webextension.svg)](https://travis-ci.org/NeApp/neon-extension-browser-webextension) |  |
| [neon-extension-destination-lastfm](https://github.com/NeApp/neon-extension-destination-lastfm)     | [![](https://img.shields.io/travis/NeApp/neon-extension-destination-lastfm.svg)](https://travis-ci.org/NeApp/neon-extension-destination-lastfm)     |  |
| [neon-extension-source-googlemusic](https://github.com/NeApp/neon-extension-source-googlemusic)     | [![](https://img.shields.io/travis/NeApp/neon-extension-source-googlemusic.svg)](https://travis-ci.org/NeApp/neon-extension-source-googlemusic)     |  |

## Build

### Production Builds

**Requirements**

 - node
 - npm
 - *git (optional)*

**Steps**

1. **Download build files**

    Clone the repository, and checkout the desired version:

    ```
    git clone git@github.com:NeApp/neon-extension-chrome.git
    git checkout (version)
    ```

    or download the release archive:

    ```
    wget https://github.com/NeApp/neon-extension-chrome/archive/(version).zip
    ```

2. **Install dependencies**

    ```
    npm install
    ```

3. **Run build**

    ```
    npm run build
    ```

    Build artifacts will be available at `build/production/`
