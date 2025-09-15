from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'core.urls', name='www'),  # main site
    host(r'student', 'users.student_urls', name='student'),
    host(r'instructor', 'users.instructor_urls', name='instructor'),
    host(r'admin', 'users.admin_urls', name='admin'),
)
