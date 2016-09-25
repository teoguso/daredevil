# Unity visualization

Proof of concept for transmitting finished radar matrix vertices to **Unity** binary via socket. 

Tested to work on **Windows 7 x64**, **Android 4.1.2** and **Android 6.0.1** (included apk file is *Honeycomb*) with **Unity v5.3.5f1** and **v5.4.1**.

Also did successful build for **Gear VR** with **Unity v5.3.5f1** and **Android 6.0.1**


### `SceneController.cs`

Script for controlling the **Unity** demo scene. Add it to an empty toplevel `GameObject`.

Instantiates 10 simple `GameObjects`, and positions them in the scene from the received *UDP data*. 

It expects a byte array of 3 * 4 * 10 bytes (3 dimensions, 4 bytes for float size, 10 = one for each object).

The script requires a *prefab* named `EchoObject`. For the tests a simple unit cube was used.

IP address is hardcoded because method for attempted auto-detection of WiFi interface doesn't work when building for *Android* doesn't work.

See [this question on stackoverflow\.com](http://gamedev.stackexchange.com/questions/130444/determine-wifi-adapter-address-on-android-with-unity-c) for details.

### `dgramsend.py`

Simple *Python* script to send 3 x 10 floats to the *UDP* port open in the Unity script. Takes IP of the device running Unity as argument.

Runs on *Python 2.7.12* and *3.5.2* at least.

### `test.apk`

*Android* package built for Meredith's phone (but with hardcoded IP address, so it's probably stale already).
