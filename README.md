Readme file for Python Jobs:

Export environent variable :
export python=/home/akash/python/


**Python jobs directory structure.**

${python}/Brace_Validator : contains source code for Brace_Validator.
${python}/External_Sorting : Contains source code, input, output file for External_Sorting(Check various parts in External_Sorting directory)


Steps to run the jobs:

**Note: env variable python should be exported and clean output directory before running pythons programs.**

Format :	For help :	python source_code.py -h <help> 
		To run : 	python source_code.py -i < inputdir> -o <outputdir> -o <other optional parameters>

1.) External_Sorting:
	python ${python}/External_Sorting/part_1/src/sort.py -i ${python}/External_Sorting/part_1/input/ -o ${python}/External_Sorting/part_1/output/
	
3.) Brace_Validator :
	python ${python}/Brace_Validator/src/brace_validator.py 


Output of jobs :

1.)  External_Sorting:
	 ${python}/External_Sorting/

3.)  Brace_Validator: On Console


