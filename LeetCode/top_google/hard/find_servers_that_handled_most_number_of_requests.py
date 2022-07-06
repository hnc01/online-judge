'''
    https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

    1606. Find Servers That Handled Most Number of Requests

    You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously.
    Each server has infinite computational capacity but cannot handle more than one request at a time.

    The requests are assigned to servers according to a specific algorithm:
    - The ith (0-indexed) request arrives.
    - If all servers are busy, the request is dropped (not handled at all).
    - If the (i % k)th server is available, assign the request to that server.
    - Otherwise, assign the request to the next available server (wrapping around the list of servers and starting
    from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server,
    then the (i+2)th server, and so on.

    You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival
    time of the ith request, and another array load, where load[i] represents the load of the ith request (the time
    it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled
    the most number of requests successfully among all the servers.

    Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.
'''
import collections
import heapq

'''
    Correct but TLE.
    
    The bottleneck: finding the next free server.
'''


class Solution:
    def busiestServers(self, k: int, arrival: [int], load: [int]) -> [int]:
        # so that we know that each point in time the load for every server
        loadPerServer = []

        # so that we know the number of requests each server handled
        requestsPerServer = []

        # to keep track of the max number of requests a server or servers have handled
        maxRequests = 0

        # freeServersCount (used later in loop):
        # so that we can keep track of how many servers are free to know
        # right away of we should look for the free servers or if we should
        # drop the new request. At start, all servers are free.

        # initially, all the servers have load = 0 => they're free
        # initially, all servers haven't handled any requests
        for i in range(0, k):
            loadPerServer[i] = 0
            requestsPerServer[i] = 0

        previousArrivalTime = 0

        for i in range(0, len(arrival)):
            # with every arrival, we need to:
            # 1- update the load for each server => reduce the load of each server depending
            # on how much time has passed since last request.
            # 2- Find a server for the new request
            timePassed = arrival[i] - previousArrivalTime

            previousArrivalTime = arrival[i]

            # with every loop we recount the number of free servers
            freeServersCount = 0

            # doing step 1
            # TODO maybe loop over only the ones we know were busy in previous iteration? (maybe also free ones?)
            # TODO the number of busy servers will only decrease between iterations before taking on a new request
            # TODO know that the server we need to assign to now is i % k, maybe in this loop keep track of smallest
            # free server before i % k AND smallest free server after i % k => that way we can avoid the below loop again
            for server in loadPerServer:
                loadPerServer[server] = max(0, loadPerServer[server] - timePassed)

                if loadPerServer[server] == 0:
                    freeServersCount += 1

            # now that we updated the load for each server, we need to find a server that
            # can handle the current request by following the algorithm (i % k)th
            # first we check if there are free servers
            if freeServersCount > 0:
                serverToAssign = i % k

                while loadPerServer[serverToAssign] > 0:
                    serverToAssign = (serverToAssign + 1) % k

                # found the server to assign this load
                loadPerServer[serverToAssign] = load[i]

                # update the number of requests handled by server serverToAssign
                requestsPerServer[serverToAssign] += 1

                maxRequests = max(maxRequests, requestsPerServer[serverToAssign])

        busiestServers = []

        for server in requestsPerServer:
            if requestsPerServer[server] == maxRequests:
                busiestServers.append(server)

        return busiestServers


'''
    Idea:
    - Instead of saving the load per server and then deciding whether the load is done based on new arrival time,
    I should translate the load into endTime => if arrival is at 2 and the load is 10, then endTime = 12.
    - When we have a new task to add to our collection, we need to mark all the servers that have endTime >= arrival[i]
    as now free servers.
    - To quickly extract the servers with closest endTime to our new arrival, we can make use of a min heap structure.
'''

'''
    Accepted
'''


class Solution2:
    def busiestServers(self, k: int, arrival: [int], load: [int]) -> [int]:
        # this binary search method will search for key and if key is not found
        # it returns the index of the smallest element greater than key
        def binarySearch(servers, key, s, e):
            while s <= e:
                mid = s + (e - s) // 2

                # Check if x is present at mid
                if servers[mid] == key:
                    return mid

                # If x is greater, ignore left half
                elif servers[mid] < key:
                    s = mid + 1

                # If x is smaller, ignore right half
                else:
                    e = mid - 1

                # If we reach here, then the element
                # was not present

            return (e + 1)

        # this will contain pairs of (endTime, serverId) | will be used as min heap
        busyServers = []

        # by default, all the servers are free
        # this is a sorted list of free servers
        freeServers = [i for i in range(0, k)]

        # so that we know the number of requests each server handled
        # by default, all the servers have 0 requests
        requestsPerServer = [0] * k

        # to keep track of the max number of requests a server or servers have handled
        maxRequests = 0

        for i in range(0, len(arrival)):
            isUpdateMade = False

            # find all the (endTime, serverId) pairs in busyServers that have endTime >= arrival[i]
            while len(busyServers) > 0 and busyServers[0][0] <= arrival[i]:
                # pop it from the heap and add it to freeServers
                endTime, serverId = heapq.heappop(busyServers)

                freeServers.append(serverId)

                isUpdateMade = True

            # if we have any free servers, then we find our next free server
            # otherwise the task of arrival[i] is dropped
            if len(freeServers) > 0:
                # now we resort our array of free servers
                # Only pay the price of resorting freeServers IF the array was updated with new free servers
                if isUpdateMade:
                    freeServers.sort()

                # now we find our next free server
                nextFreeServerIndex = binarySearch(freeServers, i % k, 0, len(freeServers) - 1)

                if nextFreeServerIndex >= len(freeServers):
                    # loop back to beginning of free array because no server with ID > than the server we need is free
                    nextFreeServerIndex = 0

                # task the free server we found
                heapq.heappush(busyServers, (arrival[i] + load[i], freeServers[nextFreeServerIndex]))

                # update the number of requests this server has had
                requestsPerServer[freeServers[nextFreeServerIndex]] += 1

                # update our value of max requests seen so far
                maxRequests = max(maxRequests, requestsPerServer[freeServers[nextFreeServerIndex]])

                # remove freeServers[nextFreeServerIndex] from freeServers
                freeServers.pop(nextFreeServerIndex)

        busiestServers = []

        for i in range(0, k):
            if requestsPerServer[i] == maxRequests:
                busiestServers.append(i)

        return busiestServers

# print(Solution2().busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))
# print(Solution2().busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))
# print(Solution2().busiestServers(k = 3, arrival = [1,2,3], load = [10,12,11]))
# print(Solution2().busiestServers(k=3, arrival=[1, 3, 5, 8], load=[2, 4, 5, 12]))
