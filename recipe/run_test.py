import os

# Importing tabpfn fails when 'CI' environment variable is set to anything else than 'true' or 'false' (e.g., 'azure').
os.environ["CI"] = "true"

import tabpfn
