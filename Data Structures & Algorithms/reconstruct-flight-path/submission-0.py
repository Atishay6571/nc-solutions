class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build adjacency list
        adj = defaultdict(list)
        for depart, arrival in tickets:
            adj[depart].append(arrival)

        # CHANGED: Sort once here instead of every DFS call
        # Since you'll always pop the smallest lexical destination.
        for depart in adj:
            adj[depart].sort(reverse=True)

        totalTrips = len(tickets)
        trip = ["JFK"]

        def dfs(depart):

            # CHANGED: Base case is when ALL tickets have been used.
            if len(trip) == totalTrips + 1:
                return True

            # CHANGED: Need to try EVERY outgoing edge.
            # You can't just pop one edge and hope it works.
            for i in range(len(adj[depart])):

                # CHANGED: Remove one ticket (edge).
                destination = adj[depart].pop()

                # CHANGED: Since we're taking this ticket,
                # it should immediately appear in our itinerary.
                trip.append(destination)

                # CHANGED: If this branch succeeds,
                # immediately bubble True back up.
                if dfs(destination):
                    return True

                # CHANGED: Backtrack BOTH itinerary and edge.
                trip.pop()
                adj[depart].insert(0, destination)
                # (You'll need to think carefully whether insert(0)
                # is the correct restoration position.)

            return False

        dfs("JFK")
        return trip