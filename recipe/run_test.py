import os

# Importing tabpfn fails when 'CI' environment variable is set to anything other than 'true' or 'false' (e.g., 'azure').
# Ref.: https://github.com/PriorLabs/TabPFN/issues/482
os.environ["CI"] = "true"

import tabpfn
