#include <errno.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

enum { MAX_WORKERS = 8, UPDATES_PER_WORKER = 2 };

static pthread_mutex_t counter_lock = PTHREAD_MUTEX_INITIALIZER;
static unsigned counter;

static void check_pthread(int status, const char *operation)
{
    if (status != 0) {
        fprintf(stderr, "%s failed (%d)\n", operation, status);
        exit(EXIT_FAILURE);
    }
}

static void *update_counter(void *unused)
{
    (void)unused;
    for (unsigned update = 0; update < UPDATES_PER_WORKER; ++update) {
        check_pthread(pthread_mutex_lock(&counter_lock), "pthread_mutex_lock");
        ++counter;
        check_pthread(pthread_mutex_unlock(&counter_lock), "pthread_mutex_unlock");
    }
    return NULL;
}

int main(int argc, char **argv)
{
    char *end;
    long workers;
    pthread_t threads[MAX_WORKERS];

    if (argc != 2) {
        fprintf(stderr, "Usage: %s {2|4|8}\n", argv[0]);
        return EXIT_FAILURE;
    }

    errno = 0;
    workers = strtol(argv[1], &end, 10);
    if (errno != 0 || end == argv[1] || *end != '\0' ||
        (workers != 2 && workers != 4 && workers != 8)) {
        fprintf(stderr, "Worker count must be 2, 4, or 8\n");
        return EXIT_FAILURE;
    }

    for (long worker = 0; worker < workers; ++worker) {
        check_pthread(pthread_create(&threads[worker], NULL, update_counter, NULL),
                      "pthread_create");
    }
    for (long worker = 0; worker < workers; ++worker) {
        check_pthread(pthread_join(threads[worker], NULL), "pthread_join");
    }

    unsigned expected = (unsigned)workers * UPDATES_PER_WORKER;
    printf("workers=%ld updates_per_worker=%u counter=%u expected=%u\n",
           workers, (unsigned)UPDATES_PER_WORKER, counter, expected);
    return counter == expected ? EXIT_SUCCESS : EXIT_FAILURE;
}
