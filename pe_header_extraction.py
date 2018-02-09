
# coding: utf-8

# In[1]:

import pefile
import glob
import csv
import os
import numpy as np
import pandas as pd


# In[2]:

g=glob.glob("/home/naresh/Downloads/Project/Benign/*");


# In[3]:

d=[]


# In[4]:

for files in g:
    try:
        pe=pefile.PE(files,fast_load=True);
        d.append((files,pe.DOS_HEADER.e_magic,pe.DOS_HEADER.e_cblp,pe.DOS_HEADER.e_cp,pe.DOS_HEADER.e_crlc,pe.DOS_HEADER.e_cparhdr,pe.DOS_HEADER.e_minalloc,pe.DOS_HEADER.e_maxalloc,pe.DOS_HEADER.e_ss,pe.DOS_HEADER.e_sp,pe.DOS_HEADER.e_csum,pe.DOS_HEADER.e_ip,pe.DOS_HEADER.e_cs,pe.DOS_HEADER.e_lfarlc,pe.DOS_HEADER.e_ovno,pe.DOS_HEADER.e_oemid,pe.DOS_HEADER.e_oeminfo,pe.DOS_HEADER.e_lfanew,pe.FILE_HEADER.Machine,pe.FILE_HEADER.NumberOfSections,pe.FILE_HEADER.TimeDateStamp,pe.FILE_HEADER.PointerToSymbolTable,pe.FILE_HEADER.NumberOfSymbols,pe.FILE_HEADER.SizeOfOptionalHeader,pe.FILE_HEADER.Characteristics,pe.OPTIONAL_HEADER.MajorLinkerVersion,pe.OPTIONAL_HEADER.MinorLinkerVersion,pe.OPTIONAL_HEADER.SizeOfCode,pe.OPTIONAL_HEADER.SizeOfInitializedData,pe.OPTIONAL_HEADER.SizeOfUninitializedData,pe.OPTIONAL_HEADER.AddressOfEntryPoint,pe.OPTIONAL_HEADER.BaseOfCode,pe.OPTIONAL_HEADER.BaseOfData,pe.OPTIONAL_HEADER.ImageBase,pe.OPTIONAL_HEADER.SectionAlignment,pe.OPTIONAL_HEADER.FileAlignment,pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,pe.OPTIONAL_HEADER.MinorOperatingSystemVersion,pe.OPTIONAL_HEADER.MajorImageVersion,pe.OPTIONAL_HEADER.MinorImageVersion,pe.OPTIONAL_HEADER.MajorSubsystemVersion,pe.OPTIONAL_HEADER.MinorSubsystemVersion,pe.OPTIONAL_HEADER.Reserved1,pe.OPTIONAL_HEADER.SizeOfImage,pe.OPTIONAL_HEADER.SizeOfHeaders,pe.OPTIONAL_HEADER.CheckSum,pe.OPTIONAL_HEADER.Subsystem,pe.OPTIONAL_HEADER.DllCharacteristics,pe.OPTIONAL_HEADER.SizeOfStackReserve,pe.OPTIONAL_HEADER.SizeOfStackCommit,pe.OPTIONAL_HEADER.SizeOfHeapReserve,pe.OPTIONAL_HEADER.SizeOfHeapCommit,pe.OPTIONAL_HEADER.LoaderFlags,pe.OPTIONAL_HEADER.NumberOfRvaAndSizes,0))
    except Exception as e:
        d.append((files,pe.DOS_HEADER.e_magic,pe.DOS_HEADER.e_cblp,pe.DOS_HEADER.e_cp,pe.DOS_HEADER.e_crlc,pe.DOS_HEADER.e_cparhdr,pe.DOS_HEADER.e_minalloc,pe.DOS_HEADER.e_maxalloc,pe.DOS_HEADER.e_ss,pe.DOS_HEADER.e_sp,pe.DOS_HEADER.e_csum,pe.DOS_HEADER.e_ip,pe.DOS_HEADER.e_cs,pe.DOS_HEADER.e_lfarlc,pe.DOS_HEADER.e_ovno,pe.DOS_HEADER.e_oemid,pe.DOS_HEADER.e_oeminfo,pe.DOS_HEADER.e_lfanew,pe.FILE_HEADER.Machine,pe.FILE_HEADER.NumberOfSections,pe.FILE_HEADER.TimeDateStamp,pe.FILE_HEADER.PointerToSymbolTable,pe.FILE_HEADER.NumberOfSymbols,pe.FILE_HEADER.SizeOfOptionalHeader,pe.FILE_HEADER.Characteristics,pe.OPTIONAL_HEADER.MajorLinkerVersion,pe.OPTIONAL_HEADER.MinorLinkerVersion,pe.OPTIONAL_HEADER.SizeOfCode,pe.OPTIONAL_HEADER.SizeOfInitializedData,pe.OPTIONAL_HEADER.SizeOfUninitializedData,pe.OPTIONAL_HEADER.AddressOfEntryPoint,pe.OPTIONAL_HEADER.BaseOfCode,np.NaN,pe.OPTIONAL_HEADER.ImageBase,pe.OPTIONAL_HEADER.SectionAlignment,pe.OPTIONAL_HEADER.FileAlignment,pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,pe.OPTIONAL_HEADER.MinorOperatingSystemVersion,pe.OPTIONAL_HEADER.MajorImageVersion,pe.OPTIONAL_HEADER.MinorImageVersion,pe.OPTIONAL_HEADER.MajorSubsystemVersion,pe.OPTIONAL_HEADER.MinorSubsystemVersion,pe.OPTIONAL_HEADER.Reserved1,pe.OPTIONAL_HEADER.SizeOfImage,pe.OPTIONAL_HEADER.SizeOfHeaders,pe.OPTIONAL_HEADER.CheckSum,pe.OPTIONAL_HEADER.Subsystem,pe.OPTIONAL_HEADER.DllCharacteristics,pe.OPTIONAL_HEADER.SizeOfStackReserve,pe.OPTIONAL_HEADER.SizeOfStackCommit,pe.OPTIONAL_HEADER.SizeOfHeapReserve,pe.OPTIONAL_HEADER.SizeOfHeapCommit,pe.OPTIONAL_HEADER.LoaderFlags,pe.OPTIONAL_HEADER.NumberOfRvaAndSizes,0))
        pass


# In[5]:

g=glob.glob("/home/naresh/Downloads/Project/Virus.Win/*");


# In[6]:

for files in g:
    try:
        pe=pefile.PE(files,fast_load=True);
        d.append((files,pe.DOS_HEADER.e_magic,pe.DOS_HEADER.e_cblp,pe.DOS_HEADER.e_cp,pe.DOS_HEADER.e_crlc,pe.DOS_HEADER.e_cparhdr,pe.DOS_HEADER.e_minalloc,pe.DOS_HEADER.e_maxalloc,pe.DOS_HEADER.e_ss,pe.DOS_HEADER.e_sp,pe.DOS_HEADER.e_csum,pe.DOS_HEADER.e_ip,pe.DOS_HEADER.e_cs,pe.DOS_HEADER.e_lfarlc,pe.DOS_HEADER.e_ovno,pe.DOS_HEADER.e_oemid,pe.DOS_HEADER.e_oeminfo,pe.DOS_HEADER.e_lfanew,pe.FILE_HEADER.Machine,pe.FILE_HEADER.NumberOfSections,pe.FILE_HEADER.TimeDateStamp,pe.FILE_HEADER.PointerToSymbolTable,pe.FILE_HEADER.NumberOfSymbols,pe.FILE_HEADER.SizeOfOptionalHeader,pe.FILE_HEADER.Characteristics,pe.OPTIONAL_HEADER.MajorLinkerVersion,pe.OPTIONAL_HEADER.MinorLinkerVersion,pe.OPTIONAL_HEADER.SizeOfCode,pe.OPTIONAL_HEADER.SizeOfInitializedData,pe.OPTIONAL_HEADER.SizeOfUninitializedData,pe.OPTIONAL_HEADER.AddressOfEntryPoint,pe.OPTIONAL_HEADER.BaseOfCode,pe.OPTIONAL_HEADER.BaseOfData,pe.OPTIONAL_HEADER.ImageBase,pe.OPTIONAL_HEADER.SectionAlignment,pe.OPTIONAL_HEADER.FileAlignment,pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,pe.OPTIONAL_HEADER.MinorOperatingSystemVersion,pe.OPTIONAL_HEADER.MajorImageVersion,pe.OPTIONAL_HEADER.MinorImageVersion,pe.OPTIONAL_HEADER.MajorSubsystemVersion,pe.OPTIONAL_HEADER.MinorSubsystemVersion,pe.OPTIONAL_HEADER.Reserved1,pe.OPTIONAL_HEADER.SizeOfImage,pe.OPTIONAL_HEADER.SizeOfHeaders,pe.OPTIONAL_HEADER.CheckSum,pe.OPTIONAL_HEADER.Subsystem,pe.OPTIONAL_HEADER.DllCharacteristics,pe.OPTIONAL_HEADER.SizeOfStackReserve,pe.OPTIONAL_HEADER.SizeOfStackCommit,pe.OPTIONAL_HEADER.SizeOfHeapReserve,pe.OPTIONAL_HEADER.SizeOfHeapCommit,pe.OPTIONAL_HEADER.LoaderFlags,pe.OPTIONAL_HEADER.NumberOfRvaAndSizes,1))
    except Exception as e:
        d.append((files,pe.DOS_HEADER.e_magic,pe.DOS_HEADER.e_cblp,pe.DOS_HEADER.e_cp,pe.DOS_HEADER.e_crlc,pe.DOS_HEADER.e_cparhdr,pe.DOS_HEADER.e_minalloc,pe.DOS_HEADER.e_maxalloc,pe.DOS_HEADER.e_ss,pe.DOS_HEADER.e_sp,pe.DOS_HEADER.e_csum,pe.DOS_HEADER.e_ip,pe.DOS_HEADER.e_cs,pe.DOS_HEADER.e_lfarlc,pe.DOS_HEADER.e_ovno,pe.DOS_HEADER.e_oemid,pe.DOS_HEADER.e_oeminfo,pe.DOS_HEADER.e_lfanew,pe.FILE_HEADER.Machine,pe.FILE_HEADER.NumberOfSections,pe.FILE_HEADER.TimeDateStamp,pe.FILE_HEADER.PointerToSymbolTable,pe.FILE_HEADER.NumberOfSymbols,pe.FILE_HEADER.SizeOfOptionalHeader,pe.FILE_HEADER.Characteristics,pe.OPTIONAL_HEADER.MajorLinkerVersion,pe.OPTIONAL_HEADER.MinorLinkerVersion,pe.OPTIONAL_HEADER.SizeOfCode,pe.OPTIONAL_HEADER.SizeOfInitializedData,pe.OPTIONAL_HEADER.SizeOfUninitializedData,pe.OPTIONAL_HEADER.AddressOfEntryPoint,pe.OPTIONAL_HEADER.BaseOfCode,np.NaN,pe.OPTIONAL_HEADER.ImageBase,pe.OPTIONAL_HEADER.SectionAlignment,pe.OPTIONAL_HEADER.FileAlignment,pe.OPTIONAL_HEADER.MajorOperatingSystemVersion,pe.OPTIONAL_HEADER.MinorOperatingSystemVersion,pe.OPTIONAL_HEADER.MajorImageVersion,pe.OPTIONAL_HEADER.MinorImageVersion,pe.OPTIONAL_HEADER.MajorSubsystemVersion,pe.OPTIONAL_HEADER.MinorSubsystemVersion,pe.OPTIONAL_HEADER.Reserved1,pe.OPTIONAL_HEADER.SizeOfImage,pe.OPTIONAL_HEADER.SizeOfHeaders,pe.OPTIONAL_HEADER.CheckSum,pe.OPTIONAL_HEADER.Subsystem,pe.OPTIONAL_HEADER.DllCharacteristics,pe.OPTIONAL_HEADER.SizeOfStackReserve,pe.OPTIONAL_HEADER.SizeOfStackCommit,pe.OPTIONAL_HEADER.SizeOfHeapReserve,pe.OPTIONAL_HEADER.SizeOfHeapCommit,pe.OPTIONAL_HEADER.LoaderFlags,pe.OPTIONAL_HEADER.NumberOfRvaAndSizes,1))
        pass


# In[7]:

data= pd.DataFrame(d, columns=('FileName','DOS_HEADER.e_magic','DOS_HEADER.e_cblp','DOS_HEADER.e_cp','DOS_HEADER.e_crlc','DOS_HEADER.e_cparhdr','DOS_HEADER.e_minalloc','DOS_HEADER.e_maxalloc','DOS_HEADER.e_ss','DOS_HEADER.e_sp','DOS_HEADER.e_csum','DOS_HEADER.e_ip','DOS_HEADER.e_cs','DOS_HEADER.e_lfarlc','DOS_HEADER.e_ovno','DOS_HEADER.e_oemid','DOS_HEADER.e_oeminfo','DOS_HEADER.e_lfanew','FILE_HEADER.Machine','FILE_HEADER.NumberOfSections','FILE_HEADER.TimeDateStamp','FILE_HEADER.PointerToSymbolTable','FILE_HEADER.NumberOfSymbols','FILE_HEADER.SizeOfOptionalHeader','FILE_HEADER.Characteristics','OPTIONAL_HEADER.MajorLinkerVersion','OPTIONAL_HEADER.MinorLinkerVersion','OPTIONAL_HEADER.SizeOfCode','OPTIONAL_HEADER.SizeOfInitializedData','OPTIONAL_HEADER.SizeOfUninitializedData','OPTIONAL_HEADER.AddressOfEntryPoint','OPTIONAL_HEADER.BaseOfCode','OPTIONAL_HEADER.BaseOfData','OPTIONAL_HEADER.ImageBase','OPTIONAL_HEADER.SectionAlignment','OPTIONAL_HEADER.FileAlignment','OPTIONAL_HEADER.MajorOperatingSystemVersion','OPTIONAL_HEADER.MinorOperatingSystemVersion','OPTIONAL_HEADER.MajorImageVersion','OPTIONAL_HEADER.MinorImageVersion','OPTIONAL_HEADER.MajorSubsystemVersion','OPTIONAL_HEADER.MinorSubsystemVersion','OPTIONAL_HEADER.Reserved1','OPTIONAL_HEADER.SizeOfImage','OPTIONAL_HEADER.SizeOfHeaders','OPTIONAL_HEADER.CheckSum','OPTIONAL_HEADER.Subsystem','OPTIONAL_HEADER.DllCharacteristics','OPTIONAL_HEADER.SizeOfStackReserve','OPTIONAL_HEADER.SizeOfStackCommit','OPTIONAL_HEADER.SizeOfHeapReserve','OPTIONAL_HEADER.SizeOfHeapCommit','OPTIONAL_HEADER.LoaderFlags','OPTIONAL_HEADER.NumberOfRvaAndSizes','Malicious'))


# In[8]:

data.head()


# In[9]:

data.info()


# In[10]:

data.isnull().sum()


# In[11]:

data.to_csv("pe_header_allfiles.csv")


# In[ ]:



