import sys
import os
import getpass
text_file = open("rc.conf", "w")
text_file.write("[GC]\ntype = drive\nscope = drive\nservice_account_file = accounts/1.json\nservice_account_file_path = accounts/")
text_file.close()
username = getpass.getuser()
print('\033[1;31;40mHey,Sexy! wanna clone some TBs?\nLets Get you started\n')
FRflag = ("--drive-server-side-across-configs --ignore-existing --stats=1s --stats-one-line -vP --checkers=256 --transfers=256 --drive-pacer-min-sleep=1ms --drive-pacer-burst=5000 --check-first")
SRflag = ("--transfers 50 -v --stats-one-line --stats=15s --ignore-existing --drive-server-side-across-configs --drive-chunk-size 128M --drive-acknowledge-abuse --drive-keep-revision-forever")
vrflag = ('--fast-list --verbose=2 --checkers=64 --transfers=128 -q')
rmflag = ('--drive-use-trash=true --verbose=2 --fast-list')
if os.path.isdir('accounts'):
  print('\n')
else:
  print("\033[1;31;40m Account folder containing SA's JSON not found\n")
  sys.exit()
print('\033[1;33;40mChoose what you like to do \n')  
MD = input("\033[1;36;40mA.Copy\nB.Move\nC.Sync\nD.Dedupe\nE.RemoveDirs\nF.Size\nG.Dir listing\nNOTE:Read Rclone Documentations for more info on these operations\nOperation(Chose either A/B/C/D/E/F/G): \n")
if MD == "A":
  print("\033[1;32;40mCopy Selected\nIt will COPY content from SRC to DST\n")
  SRC = input("\033[1;34;40mProvide Source Folder ID\n")
  DST = input("\033[1;34;40mProvide Destination Folder ID\n")
  cmd = ('fclone --config=rc.conf copy GC:{'+SRC+'} GC:{'+DST+'} '+FRflag)
  os.system(cmd)
elif MD == "B":
  print("\033[1;32;40mMove Selected\nIt will MOVE content from SRC to DST\n")
  SRC = input("\033[1;34;40mProvide SRC Folder ID\n")
  DST = input("\033[1;34;40mProvide DST Folder ID\n")
  cmd = ('fclone --config=rc.conf move GC:{'+SRC+'} GC:{'+DST+'} '+FRflag)
  os.system(cmd)
elif MD == "C":
  print("\033[1;32;40mSync Selected\nIt will Sync content of SRC to DST (it will delete any extra files that are there only in DST use it with caution)\n")
  SRC = input("\033[1;34;40mProvide SRC Folder ID\n")
  DST = input("\033[1;34;40mProvide DST Folder ID\n")
  cmd = ('fclone --config=rc.conf sync GC:{'+SRC+'} GC:{'+DST+'} '+FRflag)
  os.system(cmd)
elif MD == "D":
  print("\033[1;32;40mDedupe selected\nIt will delete any duplicate files present in given Folder ID [it compares md5 and naming]\n")
  DP = input("select delete mode\nA.interactive\nB.newest\nC.oldest\nD.largest\nE.smallest\n")
  SRC = input("\033[1;34;40mProvide Folder ID\n")
  if DP == "A":
     print("\033[1;32;40mInteractive Mode selected\n")
     cmd = ('fclone --config=rc.conf dedupe --dedupe-mode interactive GC:{'+SRC+'} '+vrflag)
     os.system(cmd)
  elif DP == 'B':
     print('\033[1;32;40mNewest Mode selected\n')
     cmd = ('fclone --config=rc.conf dedupe --dedupe-mode newest GC:{'+SRC+'} '+vrflag)
     os.system(cmd)   
  elif DP == 'C':
     print('\033[1;32;40mOldest Mode selected\n')
     cmd = ('fclone --config=rc.conf dedupe --dedupe-mode oldest GC:{'+SRC+'} '+vrflag)
     os.system(cmd)
  elif DP == 'D':
     print('\033[1;32;40mLargest Mode selected\n')
     cmd = ('fclone --config=rc.conf dedupe --dedupe-mode largest GC:{'+SRC+'} '+vrflag)
     os.system(cmd)
  elif DP == 'E':
     print('\033[1;32;40msmallest Mode selected\n')
     cmd = ('fclone --config=rc.conf dedupe --dedupe-mode smallest GC:{'+SRC+'} '+vrflag)
     os.system(cmd)     
elif MD == "E":
  print("\033[1;32;40mRemoveDirs Selected\nRemoves Empty Directory From the given Folder ID\n")
  SRC = input("Provide Folder ID\n") 
  cmd = ('fclone --config=rc.conf rmdirs GC:{'+SRC+'} '+rmflag)
  os.system(cmd)
elif MD == "F":
  print("\033[1;32;40mSize selected\nIt will give the Size of the folder ID\n")
  SRC = input("\033[1;34;40mProvide Folder ID\n") 
  cmd = ('fclone --config=rc.conf size GC:{'+SRC+'} ')
  os.system(cmd)
elif MD == "G":
  print("\033[1;32;40mDirectory Listing\nIt will list the content of the give folder ID into text named file.txt\n")
  if os.path.isfile('file.txt'):
    os.remove("file.txt")
    print("File.txt Removed!")
  SRC = input("\033[1;34;40mProvide Folder ID\n") 
  cmd = ('fclone --config=rc.conf ls GC:{'+SRC+'} >> file.txt')  
  os.system(cmd)  
else :
  print ("\033[1;31;40mERROR!!!\n")
