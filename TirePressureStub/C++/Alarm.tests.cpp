#include "Alarm.hpp"
#include "StubSensor.hpp"
#include <gmock/gmock.h>

using namespace ::testing;

namespace {

TEST(Alarm, Foobar)
{
    StubSensor stubSensor;
    ON_CALL(stubSensor, popNextPressurePsiValue())
                .WillByDefault(Return(16));

    Alarm alarm(&stubSensor);
    alarm.check();

    ASSERT_THAT(alarm.isAlarmOn(), Eq(true));

}


}