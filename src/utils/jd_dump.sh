#! /bin/bash

destination_dir = "/home/ruchirich/Documents/repositories/career-ai/data/jd_dump"

cp /home/ruchirich/Documents/Personal/Career/Apping/Winter-2024/WIP/**/*.pdf "/home/ruchirich/Documents/repositories/career-ai/data/jd_dump"
    # -type f -iname "*.pdf" \
    # ! -iname "Resume_Ruchir_Attri.pdf" \
    # -exec cp {} "$destination_dir" \;

cp /home/ruchirich/Documents/Personal/Career/Apping/Winter-2024/WIP/**/**/*.pdf "/home/ruchirich/Documents/repositories/career-ai/data/jd_dump" 
    # -type f -iname "*.pdf" \
    # ! -iname "Resume_Ruchir_Attri.pdf" \
    # -exec cp {} "$destination_dir" \;

cp /home/ruchirich/Documents/Personal/Career/Apping/Winter-2024/WIP/Applied/**/*.pdf "/home/ruchirich/Documents/repositories/career-ai/data/jd_dump" 
    # -type f -iname "*.pdf" \
    # ! -iname "Resume_Ruchir_Attri.pdf" \
    # -exec cp {} "$destination_dir" \;

cp /home/ruchirich/Documents/Personal/Career/Apping/Winter-2024/WIP/Applied/**/**/*.pdf "/home/ruchirich/Documents/repositories/career-ai/data/jd_dump" 
    # -type f -iname "*.pdf" \
    # ! -iname "Resume_Ruchir_Attri.pdf" \
    # -exec cp {} "$destination_dir" \;

# echo "All PDFs have been copied except 'Resume_Ruchir_Attri.pdf'."