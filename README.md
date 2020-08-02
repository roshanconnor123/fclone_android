# Fclone_android
🔴 Just another Android Port of [Fclone](https://github.com/mawaya/rclone)

🔷 Fclone is just another Tool like Autorclone/Folderclone/Gclone to bypass the 750GB limit by google (more optimised for speed)

## 📦 Pre-requisites:-
1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en_IN%20%20) - Remember to enable storage Permission by going to settings

2. Install Python & Wget In Termux
```
pkg install python && pkg install wget
```
3. Downloaded Service Accounts (SAs) - Generate them using [Autorclone](https://github.com/xyou365/AutoRclone) or [Folderclone](https://github.com/Spazzlo/folderclone)

   Android Friendly Guide for Autorclone - [Follow this](https://telegra.ph/Autorclone-in-Android-Termux-06-30)
## 💊 Installation:-
1. Run the code in yout termux - It will install Fclone
```
wget https://github.com/roshanconnor123/fclone_android.git && mv /fclone_android/fclone /data/data/com.termux/files/usr/bin/fclone && chmod 777 /data/data/com.termux/files/usr/bin/fclone && fclone version
```

2. Create a Folder in your Internal storage and name it as **Fclone**

3. Copy the accounts Folder from our Autorclone/Folder (Which you had setup in your Phone or PC before) and Paste it in newly created **Fclone** Folder

4. Download this File 

[<p align="center"><img src="https://image.freepik.com/free-vector/download-button-white-background_97458-63.jpg" width="280" height="180"></p>](https://www23.zippyshare.com/v/k4ddLYlE/file.html)

5. Move it to newly created **Fclone** Folder
## 💣 Running Fclone
Just run this command everytime in your termux
```
cd /sdcard/fclone && python fc.py
```
Now Follow what you see in you screen and choose what you wish to do - Copy,Move etc 
## Credits:
👦 [Fclone official repo](https://github.com/mawaya/rclone)

👧 [EK](https://t.me/everykenyan)

👨 [Ansh Mittal](https://t.me/iamAnshMittal)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/roshanconnor123/fclone_android/blob/master/LICENSE) file for details
