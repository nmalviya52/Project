Malicious executable detection using machine learning.

Workflow:

1.Extracted PE files header - pe_header_extraction.py <br>
2.Extracted all the function calls - functioncall_extraction.py <br>
3.Extracted DLL calls from all files - DLL_Files_List_Extraction.py <br>
4.Data generation using DLL feature set - DLLFiles_Data_Generation.py <br>
5.Data generation using function calls feature set - Functioncall_data_generation.py <br>	
6.Merging all data fields - merge_all_fields_data.py <br>
7.Separated Training and testing data - training_testing_data_separation.py <br>
8.Features pruning using Information Gain - featureselecting_informationgain.py <br>
9.Initial Accuracy Calculation. - testing_accuracy.py <br>
