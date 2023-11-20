## 2023-08-07

- An abbreviated Steering Council (Emily and Thomas) met with Łukasz, the Developer-in-Residence, and discussed:
    - The process and requirements for enforcing PR reviews and decided to enforce reviews on PRs that are labeled as features. If you don’t want a review, add the `ci:skip-review` label.
    - The status of the Deputy DiR hiring and interview process.
    - Updates to the CLA bot, which are almost complete.

## 2023-08-14

- The Steering Council had an abbreviated meeting today, Pablo was traveling and Emily had jury duty.
- The SC met with Łukasz, the Developer-in-Residence, and discussed:
    - Next steps from our discussions and external discussions regarding dtrace.
    - Requiring code review on PRs. The implementation for requiring code reviews seems doable.
    - Hiring for the Deputy DiR position.
- The SC discussed budget and resources for mentoring support for core developers.
- The SC discussed the Core Developer Sprint in Brno, including hotel bookings and financial support for attendance.
- The SC discussed using Plausible for [docs.python.org](http://docs.python.org). The original test worked well and the WG would like to move forward with this. Costs for using the hosted version will be researched before a final decision is made, though hosted is preferred over self-hosted.

## 2023-08-21

- The Steering Council met with Łukasz, the Developer-in-Residence, and discussed:
    - The status of hiring for the Deputy DiR position.
    - Fixes for the CLA bot, which have been deployed.
    - The status of the 3.11 release; this is being held for the CVE in SSL.
    - The status of the code review requirement implementation for GitHub; this is next on his list.
- The SC discussed the Core Developer Sprint in Brno to ensure that people can receive financial support if needed even if deadlines for responses are tight.
- The SC continued to discuss [PEP 703 (Making the Global Interpreter Lock Optional in CPython)](https://peps.python.org/pep-0703/).

## 2023-08-28

- The Steering Council discussed the status of hiring for the Deputy Developer in Residence position and began reviewing the final list of candidates.
- The SC checked in on the status of 2FA for GitHub. There is still an outstanding bot that needs to be updated for compliance. Some organizations have had the 2FA requirement automatically rolled out with a 4-week notice, which should be plenty of time if it hits before we’re ready.
- The SC discussed [PEP 713 (Callable Modules)](https://peps.python.org/pep-0713/) and decided to [reject it,](https://github.com/python/steering-council/issues/191#issuecomment-1705562126) as the changes are not entirely net-positive.
