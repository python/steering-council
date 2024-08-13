# steering-council

This repo contains activity updates, process, and planning information for the Python Steering Council.

## Office Hours

The Steering Council has office hours for anyone in the community that wants to
discuss something with the Steering Council. Office hours are bookable
half-hour video calls at the start of our regular weekly meeting. Currently
it’s 30 minutes on Wednesday, 17:30 GMT (check your timezone [here](https://www.timebie.com/std/gmt.php?q=17.5)).

These meetings can be used by Core Devs, PEP authors and anyone else
contributing to Python to discuss things they want to discuss with the Steering
Council, when email or a GitHub ticket is for whatever reason not as desirable.

Scheduling is done through [Google Calendar](https://calendar.google.com/calendar/selfsched?sstoken=UUtnZXJMbl9OM3J3fGRlZmF1bHR8YWE1ZDg2MWUyZTIwYTI0NDFlNjVlOTM4Y2U3NjU2MDk). When booking a slot, please make
sure to do so at least 3 days in advance, and if possible include the topic in
the appointment so we can be prepared. For longer chats, different schedules
(we realise the current time isn’t always good for everyone), or pressing
matters, contact us directly. We can always arrange something else.

## Updates

These updates provide high level information about the Steering Council's
activities. [Subscribe to updates in your feedreader via the Atom 
feed for repository commits](https://github.com/python/steering-council/commits/main.atom).

<!-- [[[cog
import glob
filenames = sorted(glob.glob("updates/*steering-council-update.md"))
for filename in filenames:
    date = (
        filename.removeprefix("updates/")
        .removesuffix("steering-council-update.md")
        .rstrip("-_")
    )
    print(f"- [{date}]({filename})")
]]] -->
- [2019-02-15](updates/2019-02-15_steering-council-update.md)
- [2019-02-26](updates/2019-02-26_steering-council-update.md)
- [2019-04-26](updates/2019-04-26_steering-council-update.md)
- [2019-07-08](updates/2019-07-08_steering-council-update.md)
- [2019-11-09](updates/2019-11-09-steering-council-update.md)
- [2020-01-06](updates/2020-01-06-steering-council-update.md)
- [2020-11-02](updates/2020-11-02-steering-council-update.md)
- [2021-01](updates/2021-01-steering-council-update.md)
- [2021-02](updates/2021-02-steering-council-update.md)
- [2021-03](updates/2021-03-steering-council-update.md)
- [2021-04](updates/2021-04-steering-council-update.md)
- [2021-05](updates/2021-05-steering-council-update.md)
- [2021-06](updates/2021-06-steering-council-update.md)
- [2021-07](updates/2021-07-steering-council-update.md)
- [2021-08](updates/2021-08-steering-council-update.md)
- [2021-09](updates/2021-09-steering-council-update.md)
- [2021-10](updates/2021-10-steering-council-update.md)
- [2021-11](updates/2021-11-steering-council-update.md)
- [2021-12](updates/2021-12-steering-council-update.md)
- [2022-01](updates/2022-01-steering-council-update.md)
- [2022-02](updates/2022-02-steering-council-update.md)
- [2022-03](updates/2022-03-steering-council-update.md)
- [2022-04](updates/2022-04-steering-council-update.md)
- [2022-05](updates/2022-05-steering-council-update.md)
- [2022-06](updates/2022-06-steering-council-update.md)
- [2022-07](updates/2022-07-steering-council-update.md)
- [2022-08](updates/2022-08-steering-council-update.md)
- [2022-09](updates/2022-09-steering-council-update.md)
- [2022-10](updates/2022-10-steering-council-update.md)
- [2022-11](updates/2022-11-steering-council-update.md)
- [2022-12](updates/2022-12-steering-council-update.md)
- [2023-01](updates/2023-01-steering-council-update.md)
- [2023-02](updates/2023-02-steering-council-update.md)
- [2023-03](updates/2023-03-steering-council-update.md)
- [2023-04](updates/2023-04-steering-council-update.md)
- [2023-05](updates/2023-05-steering-council-update.md)
- [2023-06](updates/2023-06-steering-council-update.md)
- [2023-07](updates/2023-07-steering-council-update.md)
- [2023-08](updates/2023-08-steering-council-update.md)
- [2023-09](updates/2023-09-steering-council-update.md)
- [2023-10](updates/2023-10-steering-council-update.md)
- [2024-07](updates/2024-07-steering-council-update.md)
<!-- [[[end]]] -->

## Process

These informational documents are collected here to aid the present and
future Steering Council members.

- [Onboarding new members](process/onboarding.md)
- [Best practices for effective governance](process/best-practices.md)

## Reference

- [PEP 1 PEP Purpose and Guidelines](https://peps.python.org/pep-0001/)
- [PEP 13 Python Language Governance](https://peps.python.org/pep-0013/) (including [list of current Steering Council members](https://peps.python.org/pep-0013/#current-steering-council))
- [PEP 8001 Python Governance Voting Process](https://peps.python.org/pep-8001/)
- [PEP 8016 The Steering Council Model](https://peps.python.org/pep-8016/)
- [PEP 8100 January 2019 steering council election](https://peps.python.org/pep-8100/)
- [PEP 8101 December 2019 steering council election](https://peps.python.org/pep-8101/)
- [PEP 8102 2021 Term steering council election](https://peps.python.org/pep-8102/)
- [PEP 8103 2022 Term steering council election](https://peps.python.org/pep-8103/)
- [PEP 8104 2023 Term steering council election](https://peps.python.org/pep-8104/)
- [PEP 8105 2024 Term steering council election](https://peps.python.org/pep-8105/)
