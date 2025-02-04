try:
    from QA_Venom.decorators import check_file_upload
except ImportError:
    def check_file_upload(func):
        return func

#Test decorator
@check_file_upload
def upload_file():
    print("Uploading fiel to Azure Blob Storage")
    return True