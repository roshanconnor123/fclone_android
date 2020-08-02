# Fclone_android
🔴 Just another Android Port of [Fclone](https://github.com/mawaya/rclone)

🔷 Fclone is just another Tool like Autorclone/Folderclone/Gclone to bypass the 750GB limit by google (more optimised for speed)

## 📦 Pre-requisites:-
1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en_IN%20%20) - Remember to enable storage Permission by going to settings

2. Install Python & Git In Termux
```
pkg install python git
```
3. Downloaded Service Accounts (SAs) - Generate them using [Autorclone](https://github.com/xyou365/AutoRclone) or [Folderclone](https://github.com/Spazzlo/folderclone)

   Android Friendly Guide for Autorclone - [Follow this](https://telegra.ph/Autorclone-in-Android-Termux-06-30)
## 💊 Installation:-
1. Run the code in yout termux - It will install Fclone
```
mkdir /sdcard/fclone/ && git clone https://github.com/roshanconnor123/fclone_android && mv fclone_android/fclone /data/data/com.termux/files/usr/bin/fclone && chmod 777 /data/data/com.termux/files/usr/bin/fclone && mv fclone_android/fc.py /sdcard/fclone/ && fclone version
```
2. You can see that a new Folder called **fclone** is created in your internal storage

3. Copy the accounts Folder from our Autorclone/Folderclone Folder (Which you had setup in your Phone or PC before) and Paste it in newly created **fclone** Folder in your Internal Storage

4. Open accounts Folder and Rename any one of the jsons as 1.json
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

👨 [Krishne](https://t.me/krishne)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/roshanconnor123/fclone_android/blob/master/LICENSE) file for details
