# Submission Notes

I went through this in phases - set up the project first, got the data model and admin working, then built the list/filter view, then create, then update status, and tested each part before moving to the next one. Wanted to catch issues early instead of debugging everything all at once at the end. Styling came last, once I knew and already validated all of the functionalities that are needed to be made. Once this was okay, then testing common cases and also edge cases were the final steps along with final polishing of the UI design.

## Assumptions I Made

- A refund amount of ₱0 or negative doesn't make sense as a request, so I blocked that at the form level. You'll get a validation error if you try to submit one.
- New refund requests should always start as Pending. I didn't want whoever's creating a request to be able to set it straight to Approved or Refunded on entry.
- Updating a request's status is a separate action from editing its other details (name, email, amount, reason). Didn't want one form doing both, since those are different real-world actions for a support agent.

## Improvements I Added On Top of the Requirements

- Color-coded status badges (Pending, Approved, Rejected, Refunded) so it's easier to scan the list at a glance
- Styled the whole thing using Regent Business Process's brand colors instead of default Bootstrap blue
- Server-side validation blocking zero or negative refund amounts
- Empty state message when a filter has no matching results, instead of just a blank table

## Known Limitations

- No login or authentication - anyone with the link can view or change data
- No delete function - left this out on purpose since it wasn't part of the requirements. For something refund-related, I'd rather not have permanent deletion without thinking it through more first (a soft delete or audit trail would make more sense than just removing records)
- No pagination yet - fine for the amount of data here, but would matter once there's a lot more of it
- Using SQLite as-is, which works fine for this scope but I'd move to something like PostgreSQL for an actual production setup

## What I'd Improve With More Time

- Add basic authentication so only support staff can access this
- Add pagination once the list gets long
- Add some protection against accidentally double-submitting the create form (e.g. disabling the submit button after first click)
- Add sorting options (by amount or date) on top of the status filter
- Write actual automated tests for the core features instead of just manually clicking through everything