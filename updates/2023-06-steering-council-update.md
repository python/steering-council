## 2023-06-05

- Three Steering Council members were available to meet today, Emily and Pablo were traveling.
- The SC met with Łukasz, the Developer-in-Residence, and discussed:
  - The new Deputy Developer-in-Residence job description draft.
  - EuroPython coming up and Łukasz helping coordinate a core sprint there.
- Discussed all our [PEP 703 (Making the Global Interpreter Lock Optional in CPython)](https://peps.python.org/pep-0703/) thoughts.
- Discussed OpenSSL 3.x support backporting needs for older releases.
- Discussed 3.12 and 3.13 release schedule planning with Thomas (release manager hat).
- Discussed ongoing 3.12beta1 early findings as projects try it out.
- Briefly discussed support for core developer mentorship with Deb.

## 2023-06-12

- The Steering Council discussed [PEP 703 (Making the Global Interpreter Lock Optional in CPython)](https://peps.python.org/pep-0703/) extensively, with a focus on establishing a process and criteria for evaluating and deciding on the PEP.

## 2023-06-19

- The Steering Council discussed [PEP 703 (Making the Global Interpreter Lock Optional in CPython)](https://peps.python.org/pep-0703/) and decided to find out if there’s consensus among Core Devs for the idea and the specific PEP, through [a poll on discuss.python.org](https://discuss.python.org/t/poll-feedback-to-the-sc-on-making-cpython-free-threaded-and-pep-703/28540).
- The SC decided to schedule [office hours](https://discuss.python.org/t/steering-council-office-hours/28881) a half hour before the weekly meeting, as an experiment.
- The SC approved [Petr’s proposed changes](https://github.com/python/steering-council/issues/196) to [PEP 387 (Backwards Compatibility Policy)](https://peps.python.org/pep-0387/).

## 2023-06-26

- The Steering Council met with Seth Larson, the new Security Developer-in-Residence. One of Seth’s tasks is to improve the process behind the Python Security Response Team (PSRT), and to investigate the PSRT or PSF becoming a MITRE Sub-CNA, so it has authority over the reporting and ranking of CVEs. Seth will be working mostly with the PSRT team, only planning to have email discussions or ad-hoc meetings with the SC for now.
- The SC met with Łukasz, the Developer-in-Residence, and discussed:
  - Łukasz handling the macOS installer build as well as the Windows build for 3.12 beta 4.
  - His keynote at [PyCon Colombia](https://2023.pycon.co/).
  - A new EdgeDB release that should alleviate CLA bot inefficiencies.
  - EuroPython, his planned talk, the Core Dev panel, and the sprints there.
  - The Deputy Developer-in-Residence job opening, which will be posted this week.
- The SC discussed [json.AttrDict](https://github.com/python/cpython/issues/96145), which was added without review or discussion, with previous proposals having been rejected, and agreed with the [rollback](https://github.com/python/cpython/pull/105948) of it for now, at least until it can be discussed on discuss.python.org and a consensus is reached.
- The SC briefly discussed other open issues involving Python 3.12, leaving them to the Release Team to handle.
- The SC officially invited Russel Keith-Magee to the Core Dev Sprint in Brno in October.
