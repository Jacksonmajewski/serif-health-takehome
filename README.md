# Purpose

This repository contains a python script for extracting New York PPO URLs from any index file based on the CMS Transparency In Coverage table of contents JSON schema.
## Execution Steps

1. Download dependency listed in requirements.txt.
2. Download and extract from ZIP the index file you wish to query. This was the one used: https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2024-01-01_anthem_index.json.gz
3. Run the process_anthem_index function from take_home.py. The function allows users to specify an input and output filepath. By default the script outputs data to output.txt.
4. Each line in the output file contains one URL associated with New York PPO plans.


## Solution Process
When figuring out a solution to the problem, the biggest roadblock for me was understanding how to unpack such a large JSON file. The default json module was using too much memory, 
so my first thought was to try loading the data into a pandas dataframe via the read_json function, which would also allow me to explore the data more easily. However, this was also having memory errors,
so I then turned to the ijson module and was able to successfully parse the file. From manually exploring the file, I noticed I could consistently spot New York PPO plans using the description field on the file location object.
From here it was a matter of accurately extracting the correct URLs. I iterated through the file and added URLs with matching descriptions to a set in order to come up with a de-duplicated list of URLs.
Then I wrote the contents of the set into a text file for output.

The script took 888 seconds to execute on my machine. Overall, it took about 1 hour 15 minutes to complete the assignment. 

## Possible Improvements
The biggest improvement I can think of is in optimizing extracting and loading the JSON file. One thought I had was to split the file into separate chunks and to run each chunk in parallel. I think this makes the most sense if 
using a cloud provider that can run a process across clusters. Downloading the file itself also took a lot of time and bandwidth. If the file download process could also be sped up via a streaming solution, that would improve the 
extraction process.
