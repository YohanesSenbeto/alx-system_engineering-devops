 My First Database Outage

Duration: January 15, 2024, 21:00 EAT - January 16, 2024, 02:00 EAT (5 hours)

Impact: Our primary user database was unresponsive, resulting in:

User login failures (100% of users)

Inability to access user profiles and account information.

Increased support tickets and user frustration

Root Cause: Excessive disk I/O due to an accidental cron job running a full database backup every minute instead of daily.

Timeline:

21:00 EAT: Monitoring alerts triggered for high disk write latency and database connection failures.

21:05 EAT: Engineers investigated alerts and confirmed database unresponsiveness.

21:10 EAT: Initial troubleshooting focused on database server resources and network connectivity.

21:30 EAT: Log analysis revealed abnormally frequent database backup attempts.

21:45 EAT: The accidental cron job was identified and disabled.

22:00 EAT: Database recovered and user access restored.

23:00 EAT: Root cause confirmed as excessive disk I/O from the cron job.

02:00 EAT: Postmortem meeting held to discuss lessons learned and preventive measures.

Root Cause and Resolution:

The outage was caused by a faulty cron(time based scheduler) job configured to run the database backup script every minute instead of daily. This resulted in continuous, intensive disk writes, overwhelming the database and causing connection failures. The issue was resolved by immediately disabling the cron(time based scheduler) job and manually restarting the database server.

Corrective and Preventative Measures:

Improved Cron Job Management:

Implement stricter review and approval processes for new cron jobs.

Clearly document cron job schedules and purposes.

Consider sandbox environments for testing cron jobs before deployment.

Enhanced Monitoring:

Configure alerts for anomalous disk I/O activity to detect similar issues quickly.

Monitor database performance metrics (connections, queries, response times) more closely.

Automated Recovery Procedures:

Implement automated database failover to a secondary server in case of outages.

Develop scripts to quickly restart the database service or revert to backups.

Lessons Learned:

This incident highlighted the importance of:

Thorough code review and testing: Carefully testing and reviewing cron jobs before deployment can prevent such errors.

Effective monitoring and alerting: Timely alerts and comprehensive monitoring can help identify issues before they escalate.

Automation and redundancy: Automated recovery procedures and redundant infrastructure can minimize downtime and mitigate the impact of outages.

This was a valuable learning experience for the team. By implementing the corrective and preventative measures outlined above, we can significantly reduce the risk of similar outages in the future.
