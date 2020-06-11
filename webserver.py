from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse
import subprocess

app = FastAPI()

@app.post('/Codes')
async def post_string(request: Request):
    req = await request.json()
    # Handle json req to get the python code necessary to be run
    python_run = req['python_code']
    python_run_final = "'" + python_run + "'"

    print("Code to run in the container: \n {0}".format(python_run))
    try:
        #Create and run Container with python 3.8
        client_awnser_container = subprocess.run(
            "docker run python:3.7 python3 -c {0}".format(python_run_final),
            shell=True,
            capture_output=True)

        #Remove after sucessfull output
        remove_client_container = subprocess.run(
            "docker rm $(docker ps -aq -f status=exited -f status=created -q)",
            shell=True,
            capture_output=True)

        #Print the output that is going to go back to the client
        print(("The output for the client in bytecode: \n {0}").format(
            client_awnser_container.stdout))

        # Print container error in the process of deleting the container
        print(("Id of deleted container: \n {0}").format(
            remove_client_container.stdout.decode("utf-8")))

        # Print container error in the process of pulling image, creating and running container
        print(("The error output running the container: {0}").format(
            client_awnser_container.stderr.decode("utf-8")))

        # Print container error in the process of deleting the container
        print(("The error output deleting the container: {0}").format(
            remove_client_container.stderr.decode("utf-8")))

        # Final output
        output_final = client_awnser_container.stdout

        print("Docker runned and removed container after used :)")

        print("Sending via JSON the Output of the container...")

        print("Result for the client:\n{0}".format(
            output_final.decode("utf-8")))

    except Exception as e:
        print(e)

    return JSONResponse(
        content={"Container Response": output_final.decode("utf-8")})
