`/api/v1.0/entities/{id}/action`

The benefit of this approach is that ideally, we would open api documentation for the particular point in time and we would be able to see the behavior of all the endpoints for that particular version.

Behind the scenes, backend might use the same code but check the version running.

Each particular endpoint change might introduce a bump in api version.
