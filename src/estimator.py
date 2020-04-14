from math import ceil


def getDurationDays(data):
    '''convert weeks and months to days'''

    if data['periodType'] == 'weeks':
      return data['timeToElapse'] * 7
    elif data['periodType'] == 'months':
      return data['timeToElapse'] * 30
    return data['timeToElapse']


def impactEstimator(data):
    '''estimates the imapact using the data provided'''
    # challenge 1
    currentlyInfected = data['reportedCases'] * 10
    exp = getDurationDays(data) / 3
    infectionsByRequestedTime = currentlyInfected * ceil((2**exp))
    
    # challenge 2
    severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
    hospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) / severeCasesByRequestedTime
    
    # challenge 3
    casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
    casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
    dollarsInFlight = (infectionsByRequestedTime * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * getDurationDays(data)

    return {
      'currentlyInfected': ceil(currentlyInfected),
      'infectionsByRequestedTime': ceil(infectionsByRequestedTime),
      'severeCasesByRequestedTime': ceil(severeCasesByRequestedTime),
      'hospitalBedsByRequestedTime': ceil(hospitalBedsByRequestedTime),
      'casesForICUByRequestedTime': ceil(casesForICUByRequestedTime),
      'casesForVentilatorsByRequestedTime': ceil(casesForVentilatorsByRequestedTime),
      'dollarsInFlight': ceil(dollarsInFlight)
    }


def severeImactEstimator(data):
    '''estimates the severe impact using the data provided'''
    
    # challenge 1
    currentlyInfected = data['reportedCases'] * 50
    exp = getDurationDays(data) / 3
    infectionsByRequestedTime = currentlyInfected * (2**exp)
    
    # challenge 2
    severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
    hospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) / severeCasesByRequestedTime
    
    # challenge 3
    casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
    casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
    dollarsInFlight = (infectionsByRequestedTime * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * getDurationDays(data)

    return {
      'currentlyInfected': ceil(currentlyInfected),
      'infectionsByRequestedTime': ceil(infectionsByRequestedTime),
      'severeCasesByRequestedTime': ceil(severeCasesByRequestedTime),
      'hospitalBedsByRequestedTime': ceil(hospitalBedsByRequestedTime),
      'casesForICUByRequestedTime': ceil(casesForICUByRequestedTime),
      'casesForVentilatorsByRequestedTime': ceil(casesForVentilatorsByRequestedTime),
      'dollarsInFlight': ceil(dollarsInFlight)
    }


def estimator(data):
    '''collates all data for estimate functions'''

    estimate = {
      'data': data,
      'impact': impactEstimator(data),
      'severeImpact': severeImactEstimator(data)
    }
    return estimate
