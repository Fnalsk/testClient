### Getting started:
- From project dir: `docker build --tag testclient .`
- `docker run --network flask_network -d -p 5001:5001 testclient`
- The app should now be running on localhost:5001.
If that doesn't open on your browser, you can check the running docker container for the right address.

### Testing:
- This simple app exposes 2 endpoints:
  - `/test-deletion` tests the deletion of a key in the database.
  - `/test-overwrite` tests the overwriting of a value in an existing key in the database.
  
### Notes:
- Ideally you wouldn't test an app like this. Using something like pytest allows you to spin up a db with mock data
and destroy it when you're done testing, as well as integrate with CI/CD. This allows you to keep the state
of the database predictable between tests. This was only done this way because of a requirement in the take home test.