#include <iostream>
#include <cstring>

// Simple Date struct
struct Date {
    int day, month, year;
};

// Attendance record struct
struct AttendanceRecord {
    char studentID[10];
    Date* date;
    bool present;
};

// Abstract report interface
class ReportInterface {
public:
    virtual void generate(const AttendanceRecord* recs, int n) = 0;
    virtual ~ReportInterface() {}
};

// Daily attendance report
class DailyAttendanceReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override {
        if (n == 0) {
            std::cout << "No attendance records.\n";
            return;
        }
        std::cout << "Daily Attendance Report:\n";
        for (int i = 0; i < n; ++i) {
            std::cout << "StudentID: " << recs[i].studentID
                      << " | Date: " << recs[i].date->day << "/"
                      << recs[i].date->month << "/" << recs[i].date->year
                      << " | Present: " << (recs[i].present ? "Yes" : "No") << "\n";
        }
    }
};

// Trend attendance report
class TrendAttendanceReport : public ReportInterface {
public:
    void generate(const AttendanceRecord* recs, int n) override {
        if (n == 0) {
            std::cout << "No attendance records.\n";
            return;
        }
        int presentCount = 0;
        for (const AttendanceRecord* p = recs; p < recs + n; ++p) {
            if (p->present) ++presentCount;
        }
        std::cout << "Trend Attendance Report:\n";
        std::cout << "Total Records: " << n << "\n";
        std::cout << "Present: " << presentCount << "\n";
        std::cout << "Absent: " << (n - presentCount) << "\n";
        std::cout << "Attendance Rate: " << (100.0 * presentCount / n) << "%\n";
    }
};

// Add attendance record (resize array)
void addAttendance(AttendanceRecord*& recs, int& n, const AttendanceRecord& newRec) {
    AttendanceRecord* newArr = new AttendanceRecord[n + 1];
    for (int i = 0; i < n; ++i) {
        newArr[i] = recs[i];
    }
    newArr[n] = newRec;
    delete[] recs;
    recs = newArr;
    ++n;
}

// Remove attendance record by index (resize array)
void removeAttendance(AttendanceRecord*& recs, int& n, int index) {
    if (index < 0 || index >= n) return;
    AttendanceRecord* newArr = new AttendanceRecord[n - 1];
    for (int i = 0, j = 0; i < n; ++i) {
        if (i != index) newArr[j++] = recs[i];
    }
    delete[] recs;
    recs = newArr;
    --n;
}

// Helper to create a Date pointer
Date* makeDate(int d, int m, int y) {
    Date* date = new Date{d, m, y};
    return date;
}

// Clean up dynamically allocated Date pointers in AttendanceRecord array
void cleanupDates(AttendanceRecord* recs, int n) {
    for (int i = 0; i < n; ++i) {
        delete recs[i].date;
    }
}

int main() {
    int n = 0;
    AttendanceRecord* recs = nullptr;

    // Example: Add some attendance records
    AttendanceRecord r1;
    strcpy(r1.studentID, "S001");
    r1.date = makeDate(1, 6, 2024);
    r1.present = true;
    addAttendance(recs, n, r1);

    AttendanceRecord r2;
    strcpy(r2.studentID, "S002");
    r2.date = makeDate(1, 6, 2024);
    r2.present = false;
    addAttendance(recs, n, r2);

    AttendanceRecord r3;
    strcpy(r3.studentID, "S001");
    r3.date = makeDate(2, 6, 2024);
    r3.present = true;
    addAttendance(recs, n, r3);

    // Create reports array
    int reportCount = 2;
    ReportInterface** reports = new ReportInterface*[reportCount];
    reports[0] = new DailyAttendanceReport();
    reports[1] = new TrendAttendanceReport();

    // Generate reports
    for (int i = 0; i < reportCount; ++i) {
        reports[i]->generate(recs, n);
        std::cout << "----------------------\n";
    }

    // Remove a record
    removeAttendance(recs, n, 1);

    // Generate reports again
    for (int i = 0; i < reportCount; ++i) {
        reports[i]->generate(recs, n);
        std::cout << "----------------------\n";
    }

    // Cleanup
    for (int i = 0; i < reportCount; ++i) delete reports[i];
    delete[] reports;
    cleanupDates(recs, n);
    delete[] recs;

    return 0;
}
