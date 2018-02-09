Malicious executable detection using machine learning.

Workflow:

1.Extracted PE files header - pe_header_extraction.py
2.Extracted all the function calls - functioncall_extraction.py
3.Extracted DLL calls from all files - DLL_Files_List_Extraction.py
4.Data generation using DLL feature set - DLLFiles_Data_Generation.py
5.Data generation using function calls feature set - Functioncall_data_generation.py	
6.Merging all data fields - merge_all_fields_data.py
7.Separated Training and testing data - training_testing_data_separation.py
8.Features pruning using Information Gain - featureselecting_informationgain.py
9.Initial Accuracy Calculation. - testing_accuracy.py