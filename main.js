const path = require('path');
const url = require('url');

//window/app creation and event driven stuff (waiting for input from renderer)
const {app, BrowserWindow, ipcMain} = require('electron');

//create the basic display window
function createWindow() {
  win = new BrowserWindow({
    minHeight: 1000,
    minWidth: 1200,
    maxHeight: 1000,
    maxWidth: 1200,
    title: 'Blockchain Analytics',
    backgroundColor: '#edeeee',
    icon: path.join(__dirname, 'assets/icons/png/64x64.png'), //load and display dock icon (need to make one)
    show: false,
    webPreferences: {
      blinkFeatures: 'CSSStickyPosition'
    }
  });
  //load the single-page application html doc (which, in turn, loads scripts/aux.js and styles.css)
  win.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }));

  // Open the DevTools.
  //win.webContents.openDevTools()

  //when display elements are ready, show and focus on the window
  win.on('ready-to-show', function() {
    win.show();
    win.focus();
    win.maximize();
  });

  //when the window is closed, terminate the window, user, and lastSession variables
  win.on('closed', () => {
    win = null
    user = {}
    lastSession = {}
  });
}

//Start application
app.on('ready', createWindow)

//when all windows are closed, quit the entire app (this is the only relevent one for us since we have a SPA)
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

//clicking on dock icon will create a window if there isn't one already
app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (win === null) {
    createWindow();
  }
});

//when the user logs out, the user data and last session data is cleared
ipcMain.on('logout', function () {
  user = {}
  lastSession = {}
});

//required to allow for copy/paste into input fields once app is distributed
require('electron-context-menu')({
    prepend: (params, browserWindow) => [{
        label: 'Options',
        // Only show it when right-clicking images
        visible: params.mediaType === 'image'
    }]
});
