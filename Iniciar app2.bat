call .\docker3\Scripts\activate
cd code2
uvicorn app2:app --host=localhost --port="5050" --reload