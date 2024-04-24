import os
import dotenv
dotenv.load_dotenv()


def credentials_DB():

    DB_USER=os.environ['DB_USER']
    DB_PASS=os.environ['DB_PASS']
    DB_NAME=os.environ['DB_NAME']
    DB_PORT=os.environ['DB_PORT']
    DB_HOST=os.environ['DB_HOST']

    if not DB_USER and not DB_PASS:
        raise Exception(f"DB_USER AND DB_PASS not set")
    else:
        cred_info = {
            "DB_USER": DB_USER,
            "DB_PASS": DB_PASS,
            "DB_NAME": DB_NAME,
            "DB_PORT": DB_PORT,
            "DB_HOST": DB_HOST,
        }
        return cred_info

