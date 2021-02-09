### Summary
In late 2019, OSTIF facilitated a security audit of UnboundDNS. The audit was designed to locate bugs and weaknesses in design that impact the security of servers running Unbound DNS. A combination of manual code auditing, dynamic analysis using a custom fuzzing harness, and static analysis was used to perform the audit.

### Details
This effort led to a total of 48 changes in unbound that either improve security or fix minor issues that could lead to future security problems as the application grows and evolves over time. The consensus is that Unbound has greatly benefited from the work and that the users and applications that depend on it are now safer than they were prior to our work. A patch was released December 12th 2019. 

### Results
One Critical, Five High, and Five Medium severity issues were found, with an additional 39 issues that were rated as low or informational severity. 

### External References
The detailed audit results and full audit report are available for free at: https://ostif.org/our-audit-of-unbound-dns-by-x41-d-sec-full-results/
