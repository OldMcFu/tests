#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
#include <fcntl.h>
#include <sys/file.h> // Header für flock

class Lockfile {
public:
    explicit Lockfile(const std::string& filename) : filename(filename), fd(-1) {}

    ~Lockfile() {
        unlock();
    }

    bool lock() {
        fd = open(filename.c_str(), O_CREAT | O_RDWR, 0666);
        if (fd == -1) {
            std::cerr << "Failed to open lockfile: " << filename << std::endl;
            return false;
        }
        if (flock(fd, LOCK_EX) == -1) {
            std::cerr << "Failed to lock lockfile: " << filename << std::endl;
            close(fd);
            fd = -1;
            return false;
        }
        return true;
    }

    void unlock() {
        if (fd != -1) {
            flock(fd, LOCK_UN);
            close(fd);
            fd = -1;
            remove(filename.c_str());
        }
    }

private:
    std::string filename;
    int fd;
};

int main() {
    Lockfile lockfile("/tmp/mylockfile.lock");

    if (lockfile.lock()) {
        std::cout << "Lock acquired, proceeding with critical section." << std::endl;

        // Kritischer Abschnitt
        sleep(10); // Simuliere eine Arbeit, die Zeit benötigt

        std::cout << "Critical section done." << std::endl;

        lockfile.unlock();
    } else {
        std::cerr << "Could not acquire lock, exiting." << std::endl;
    }

    return 0;
}
