## 2023-10-02

- The Steering Council met with Łukasz, the Developer-in-Residence, and discussed:
    - The Deputy Developer-in-Residence interviews.
    - Ongoing work around `yield from` in generators, as well as PEPs [667](https://peps.python.org/pep-0667/)/[558](https://peps.python.org/pep-0558/).
    - Ongoing work around the buildbot master, individual buildbots and how to handle non-tier-1 configurations on tier-1 platforms like AddressSanitizer.
    - How to improve buildbot health and make people more aware of breakages they are causing on buildbots.
- The SC discussed the ongoing search for mentorship training and support.

## 2023-10-09

- An abbreviated Steering Council (Thomas, Pablo, and Greg) met informally in-person at the Core Developer Sprint in Brno.

## 2023-10-16

- An abbreviated Steering Council (Pablo and Brett) met with Łukasz, the Developer-in-Residence, and discussed updates on the different topics that he worked on at the sprint:
    - Coverage reports.
    - Updates of Miss-islington.
    - Help Yury with a MemHive (sharing between multiple interpreters).
    - General summary of what other people worked on.

## 2023-10-23

- An abbreviated Steering Council (Thomas, Emily, and Brett) recapped the recent Core Developer Sprint.
- The SC received a new proposal for mentorship support, which will be reviewed next week.
- The SC discussed the final specifics for accepting  [PEP 703 (Making the Global Interpreter Lock Optional in CPython)](https://peps.python.org/pep-0703/).
- The SC discussed the logistics of fitting tall people into small cars.

## 2023-10-30

- The Steering Council met with Łukasz, the Developer-in-Residence, and discussed:
    - Setting up buildbots for upcoming free-threading work.
    - General buildbot statuses and updates to fix buildbot slowness.
- The SC discussed their options and logistics for hiring an external person to take meeting minutes during weekly meetings and opted to defer this decision to the next SC.
- The SC confirmed that the details for the upcoming SC election are approved.
- The SC discussed [requests for the breaking change in the Tkinter method `wm_attributes()`](https://github.com/python/steering-council/issues/211) and decided that [PEP-387 (Backwards Compatibility Policy)](https://peps.python.org/pep-0387/) should apply and the change should follow a proper deprecation.
