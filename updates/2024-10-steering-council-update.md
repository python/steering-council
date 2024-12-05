# Steering Council Updates for October 2024

## 2024-10-02

Release Management:

- Preparations for next week's release underway
- [Python 3.13 RC3](https://www.python.org/downloads/release/python-3130rc3/) released with Windows installer updates and the [Incremental GC rolled back](https://discuss.python.org/t/incremental-gc-and-pushing-back-the-3-13-0-release/65285)
- Some concerns about [RC3](https://www.python.org/downloads/release/python-3130rc3/), mostly cosmetic issues to be addressed in 3.13.1
- Performance discussions: mixed reports on speed compared to 3.12

Core Developer Updates:

- Someone nominated for triaging, open vote on Discourse
- Increase in core developer numbers noted

Process Improvements:

- Discussion on requiring reviews for features in 3.13 and 3.14
- Acknowledgment of trust issues within the community
- Considering changes to discussion processes and decision-making
- Concerns about workload and response times for working groups

Community Engagement:

- Łukasz invited for Python 3.13 celebrations
- Upcoming Discord event with Pablo and Łukasz

PyREPL and Windows Issues:

- Functionality issues noted for Windows and shell support
- Discussions on function key behavior and documentation

Future Planning:

- New [PEP 2026](https://peps.python.org/pep-2026/) for calendar version to be reviewed next week
- PEP 667 [re-review](https://github.com/python/peps/pull/3845) closed
- Mentorship survey responses to be checked

Core Developer Sprints:

- Discussions about 2025 sprint location (Cambridge UK proposal)
- Considerations for accessibility and travel logistics
- Suggestion to create a document outlining sprint hosting requirements and costs

Miscellaneous:

- Office hours with another developer in residence scheduled for next week
- [PEP 2026](https://peps.python.org/pep-2026/) to be discussed next week
- Łukasz's requirement review process discussed

## 2024-10-09

Developer in Residence Discussion:

- Addressed concerns about a core developer's behavior and communication
- Discussed workload distribution and priorities
- Mentioned potential improvements for buildbots and test result tracking
- Explored ideas for better utilization of developer in residence role

Community Communication:

- Acknowledged concerns about transparency and fear within the community
- Discussed need for clearer communication about processes and decisions
- Considered ways to address misconceptions about Steering Council responsibilities

Core Developer Promotion:

- The Steering Council unanimously accepts the community vote to promote Matt Page to Core Developer

Election Process:

- Discussed implementation of STAR voting for upcoming term
- Noted need for Python Software Foundation to have 4 weeks to implement new voting tools
- Considered conducting mock elections to test new system

Python 3.13 Release:

- Announced release of [Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)

Core Developer Sprints:

- Discussed potential ARM-hosted sprint in Cambridge UK
- Considered logistics, including hotel bookings and travel arrangements
- Explored sponsorship possibilities, including potential separate corporate sponsorship for 2026

Financial Considerations:

- Discussed need for responsible budgeting aligned with non-profit status
- Mentioned adherence to US State Department guidelines for per diem and expenses
- Emphasized importance of Python Software Foundation involvement in financial decisions

Procedural Matters:

- Considered need for Call for Proposals (CFP) for future sprints
- Discussed community satisfaction and transparency in decision-making

## 2024-10-16

Developer in Residence Discussion:

- Concerns raised about collaboration and communication within the active [asyncio](https://docs.python.org/3/library/asyncio.html) developers
- Discussed the need for multiple experts in [asyncio](https://docs.python.org/3/library/asyncio.html) due to its complexity
- Emphasized the importance of aligning grant work with larger project goals

Core Developer Management:

- Discussed process for removing commit bits from inactive core devs
- Agreed to defer this discussion to the next Steering Council to avoid confusion with upcoming elections

Core Developer Sprint:

- Proceeding with ARM's offer to host in Cambridge UK
- Exploring additional sponsorship opportunities
- Clarified need to set expectations with sponsors regarding exclusivity

PEP 2026 (Calendar Versioning):

- Mixed opinions among SC members, ranging from slightly positive to slightly negative
- Noted lack of community consensus on the proposal
- Decided to defer decision to the next Steering Council

Election Process:

- Discussed need for clear timeline for upcoming Steering Council elections
- Considered using Notion Calendar for scheduling office hours. Decided to defer decision to the next Steering Council

PEP Delegation:

- Discussed process for delegating PEPs to working groups (e.g., C API working group)
- Considered whether to fully delegate decisions or just seek recommendations

Community Engagement:

- Discussed need for clearer communication about Steering Council's focus in coming months
- Considered public announcement about deferring certain PEPs to next Steering Council. Decided to respond to all PEPs that will be deferred

## 2024-10-23

Core Developer Sprint:

- Discussion about possible locations and timing for next year
- Need to open a poll for dates
- Location has good facilities including breakout rooms and cafeteria
- Host site has experience with similar events like Linux mini conference

Administrative Updates:

- Standing delegation docs PR needs review
- Need to formalize mentorship resources and working group
- Discussion about type annotations standardization
- Need to document code of conduct violation handling process

Core Developer Promotion Process:

- Need for more transparent criteria and process
- Concerns about pushing mentors too hard on promotions
- Need to balance mentor discretion with transparency

PEP Decisions:

- Decision to defer PEPs [2026](https://peps.python.org/pep-2026/) and [661](https://peps.python.org/pep-0661/) to next steering council
- Discussion about handling [PEP 761](https://peps.python.org/pep-0761/)
- Need for clarity on PEP decision timing relative to steering council election

Technical Discussions on JIT

- Concerns raised about debugging and profiling capabilities
- Discussion about JIT implementation impacts
- Need for balance between performance improvements and debugging capabilities
- Suggestion for informational PEP to lay out debugging/profiling issues

## 2024-10-30

Developer in Residence Update:

- Required reviews for PRs are now implemented, though not disruptive as no PRs are currently automatically marked as features
- Small disruption occurred due to changing required checks on main, requiring some PRs to update their branches
- "Do not merge" check was renamed for clarity
- ARM runners are being added for GitHub for Linux and Windows:
  - Windows runner temporarily on hold due to compiler issues
  - Using paid runners with ARM sponsorship arrangement
  - Cost expected to be lower than MacOS runners ($500/week)
  - ARM will reimburse costs through GitHub sponsorship

- New episode of the [core.py podcast](https://www.youtube.com/playlist?list=PLShJCpYUN3C3XrdguJiAZrQEnQGH-Sq26) released
- Work ongoing on asyncio debugging changes
  - Making changes so borrowed reference to task isn't needed on every generator
  - [_asynciomodule.c](https://github.com/python/cpython/blob/main/Modules/_asynciomodule.c) now holds list of pointers to root tasks for each interpreter

- Increased moderation challenges on Python Discourse forums recently
  - Dealing with controversial discussions about moderation
  - Some users potentially trying to provoke bans

- Another core developer was accepted into the Python Software Foundation Code of Conduct Working Group

Meeting among the Steering Council Members

- Discussion on [PEP 744 (JIT PEP)](https://peps.python.org/pep-0744/):
  - Potential change from informational to standards track PEP
  - Need to set clearer expectations and requirements
  - Concerns about debugging/profiling support

- Issues with CPython development complexity:
  - Performance-focused work making contribution harder
  - Challenge for community contributors to keep up

- Discussion of full-time developer impact:
  - Faster CPython team and Meta employees' (free-threading work) pace of changes
  - Balance between progress and community involvement
  - Review process challenges
  - Discussing if we could require non-affiliated or cross-discipline core dev reviews for a broader perspective on changes
  - Timing and responsiveness concerns
- Community involvement challenges:
  - Review workload distribution
- Election planning:
  - Timeline discussion
  - Encouraging nominations
- Approved August monthly notes for publishing
- Concerns about maintaining community accessibility
  - Documentation challenges
  - Onboarding new contributors
  - Balance between corporate and community contributions