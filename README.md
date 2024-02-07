# Title

## Table of Contents

## UX

## Features

## Languages and Technologies

## Testing

### Bugs

Bug found when adding updates to the carousel, active attribute was being set to all slides in the loop - Fixed by adding if statement to check forloop.counter == 1 to only set active to the first update slide in the loop.

Bug found where update link was not submitting the form on basket page - this was caused by empty href tags left on the links element, removing them fixed the issue.

Bug found where remove link on basket page threw an error for missing or incorrect csrf token - moving this function from the script.js file directly into the postload block on the basket.html page fixed the issue.

## Deployment

## Credits

Back to Top button - <https://codepen.io/Shiko/pen/NxpZae>
List specific field of query set - <https://www.reddit.com/r/django/comments/x4vgcs/how_to_get_all_the_ids_into_a_list/>
