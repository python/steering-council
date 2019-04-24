# Steering Council Update

Date: 2019-04-23

Steering Council updates will be posted irregularly and as needed.
We strive to post at least once every month.  We provide these updates
to foster open and transparent communication about Steering Council
activity.

## Message from the Steering Council

Sorry we've been silent for a while!  We've all been swamped with
work, but we've been meeting regularly.  Below are some of the
outcomes of our conversations.  Many of you will be happy to hear that
we've cleared the backlog of PEPs by assigning BDFL-Delegates to
almost all outstanding PEPs.  We're also appearing at PyCon US.

---

## Mandate

This section maps Steering Council (SC) activity and projects to the
mandates listed in PEP 13.

### Language

> Maintain the quality and stability of the Python language and CPython interpreter

- We've begun to explore the options for improving the interpreter in
  the future, but apart from PEP work we've not come to any
  conclusions yet.  In the coming months we hope to come up with
  guidelines and a process for evolving the interpreter, to be
  developed in close participation with the core developers and
  representatives of various user bases.

### Contributors

> Make contributing as accessible, inclusive, and sustainable as possible

- **Communications channels:** We have an array of communication
  options, depending on the context.

  - To reach core committers specifically, we will use
    python-committers@python.org.

  - To reach the entire Python developer community, we will use
    python-dev@python.org.

  - For specific requests to the SC, please use
    the public GitHub tracker at https://github.com/python/steering-council/issues.

  - To reach just the SC, you can email us at
    steering-council@python.org.

  - We will also occasionally use Discourse, at discuss.python.org (for example,
    Discourse is useful for polls and votes).

- **Issue tracker:** We've discussed PEP 581, "Using GitHub Issues for
  CPython" by Mariatta Wijaya.  We're in favor of this move, and feel
  that the transition should be professionally planned and executed.
  We're exploring ideas on how to do that (using the successful
  roll-out of the new Warehouse infrastructure for PyPI as a model).


### PEPs

> Establish appropriate decision-making processes for PEPs

- To request a PEP review, please file an issue on the
  `python/steering-council` GitHub repo.

- We've appointed BDFL-Delegates ("BDs") to a number of PEPs, after
  assuring that the proposed BD and the PEP author(s) agree on the
  appointment:

  - PEP 558 "Defined semantics for locals()", Nick Coghlan.
    *Appointed Nathaniel J. Smith as BD.*

  - PEP 497, "A standard mechanism for backward compatibility", Ed Schofield.
    *Appointed Brett Cannon as BD on behalf of the SC.*

  - PEP 387 "Backwards Compatibility Policy", Benjamin Peterson.
    *Appointed Brett Cannon as BD on behalf of the SC.*

  - PEP 554, "Multiple Interpreters in the Stdlib", Eric Snow.
    *Appointed Antoine Pitrou as BD.*

  - PEP 586, PEP 589, PEP 591 (various typing PEPs by members of the
    mypy team and others, topics Literal, TypedDict, and Final).
    *Appointed Guido van Rossum as BD.  (PEP 544, Protocols, also
    belongs in this list; Guido made himself BD last year.)*

  - PEP 578, "Python Runtime Audit Hooks", Steve Dower.
    *Appointed Christian Heimes as BD.*

  - PEPs 576, 579, 580 (competing PEPs on C function call
    optimizations by Mark Shannon and Jeroen Demeyer).
    *Appointed Petr Viktorin as BD.*

  - PEP 533, "Deterministic cleanup for iterators", Nathaniel J. Smith.
    *Appointed Yury Selivanov as BD.*

  - PEP 570, "Python Positional-Only Parameters", by Larry Hastings,
    Pablo Galindo and others.
    *Appointed Guido van Rossum as BD.  (And he approved it!)*

  - PEP 574, "Pickle protocol 5 with out-of-band data", Antoine Pitrou.
    *Appointed Nick Coghlan as BD.*

- And we've updated the status of some other PEPs:

  - PEP 557 "Data Classes", Eric V Smith.  *Marked Final.*

  - PEP 467 "Minor API improvements for binary sequences", Nick
    Coghlan, Ethan Furman.  *Deferred.*

  - PEP 573, "Module State Access from C Extension Methods", Petr
    Viktorin and others.  *Postponed to Python 3.9.*

### Interaction with PSF

> Formalize and maintain the relationship between the core team and the PSF

- The PSF Code of Conduct Workgroup is working on a revision of the CoC. Brett and Carol
  serve on the Workgroup.

- We've agreed to a panel discussion at PyCon US in Cleveland, Sunday
  morning May 5th between 9:20am and 10:00am.

### Governance

> Seek consensus among contributors and the core team before acting in a formal capacity
> Act as a "court of final appeal" for decisions where all other methods have failed.

- Established a weekly SC meeting cadence (Tuesdays 3-4pm US West Coast time).

- We proposed two updates to PEP 13, setting the voting period for new
  core devs to one week and for PEP 13 changes to two weeks.
  The vote is still ongoing on Discourse:
  https://discuss.python.org/t/vote-on-pep-13-change-to-specify-voting-time-frames/1510

---

## Reference

This reference section summarizes the Steering Council's mandate and powers.

### Mandate (PEP 13)

The steering council shall work to:

- Maintain the quality and stability of the Python language and
  CPython interpreter,
- Make contributing as accessible, inclusive, and sustainable as
  possible,
- Formalize and maintain the relationship between the core team and
  the PSF,
- Establish appropriate decision-making processes for PEPs,
- Seek consensus among contributors and the core team before acting in
  a formal capacity,
- Act as a "court of final appeal" for decisions where all other
  methods have failed.

### Powers (PEP 13)

The council has broad authority to make decisions about the project.
For example, they can:

- Accept or reject PEPs
- Enforce or update the project's code of conduct
- Work with the PSF to manage any project assets
- Delegate parts of their authority to other subcommittees or
  processes
