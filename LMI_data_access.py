from auth_helper import retrieve_auth, auto_refresh
from LMI_request_library import all_jobs, software_development
from framewrapper import today


@auto_refresh
def main():
    auth = retrieve_auth()

    for request in (
        all_jobs, 
        software_development
    ):
        response = request(auth)

        response.to_csv(f"{request.__name__}_{today()}.csv")


if __name__ == "__main__":
    main()

