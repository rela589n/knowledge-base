I need you to cover the project with tests (primarily, with Api test).
The Api test should only cover the main successful flow, not the edge cases.
If there are any edge cases worth covering (fragile code), you should create and *IntegrationTest instead (one that extends KernelTestCase) and cover it there just as you would with Api test. But first of all, focus on the Api tests for the success flow.
 
The tests should follow this pattern:

- Create: AddPostCommentFrontendApiPointTest
(/home/rela589n/Projects/opensource/example-project/src/EmployeePortal/Blog/Post/Comment/_Features/Add/Port/Api/AddPostCommentFrontendApiPointTest.php)
- Read: GetPostsListFrontendApiPointTest
(/home/rela589n/Projects/opensource/example-project/src/EmployeePortal/Blog/Post/_Features/GetList/Port/Api/GetPostsListFrontendApiPointTest.php)
- Update: EditPostCommentFrontendApiPointTest
(/home/rela589n/Projects/opensource/example-project/src/EmployeePortal/Blog/Post/Comment/_Features/Edit/Port/Api/EditPostCommentFrontendApiPointTest.php)
- Delete: DeleteCategoryFrontendApiPointTest
(/home/rela589n/Projects/opensource/example-project/src/EmployeePortal/Shop/Category/_Features/Delete/Port/Api/DeleteCategoryFrontendApiPointTest.php)

For test authentication, you should use JWTUser, just as you did for the Authentication tests.

Many tests are going to require the database to pre-contain something.
The tests must not prepare the data by themselves.
Instead, they should rely on the data loaded beforehand by the fixtures.

The tests that deal with particular entities (that must use ID in a URL or in a JSON payload) should hard-code IDs of those entities instead of querying the database to get the id.

If the ID of the entity that must be used in the test is dynamic (the fixtures might re-generate ID to the new value every time the database is re-created), the fixtures must be changed so that the ID will become static and will be suitable for tests usage.

The fixtures by themselves should not create the entities via a `new` operator.
Instead, they should rather use the entity's particular manager service.
For example, LoadAmenityData should have rather used AmenityManager instead of instantiating a `new Amenity()` in place. The fixture's `getReference()` calls can be disregarded in favor of the manager performing a find by repository.

To recap, when we need to make the fixture's entity IDs static, we should:
- use manager for its creation;
- call manager method with a DTO that accepts entity ID.

The DTO objects itself might need to be changed to accept a static ID if they don't already.
See RegisterUserCommand for an example of how the DTO should handle the id and do similarly:
/home/rela589n/Projects/opensource/example-project/src/EmployeePortal/Authentication/User/_Features/Register/Port/RegisterUserCommand.php

Endpoints that create an entity might pass the ID as part of the payload and then find the same entity from the entity manager to verify the expected state.

In the scope of this change, first of all, I want you to create the functional API tests for:
1. the Airport endpoints (App\Airport);
2. the Itinerary endpoints (App\Itinerary)
leaving the rest of the system alone.

Do not spawn more than 2 agents at a time.
