worldcup={
        "country":[
            {"name" : "india",
             "players": [
                {"name":"rohit","age":33,"role":"batsman"},
                {"name":"virat","age":32,"role":"batsman"},
                {"name":"bumrah","age":28,"role":"bowler"},
                {"name":"jadeja","age":30,"role":"allrounder"},
                {"name":"ashwin","age":34,"role":"bowler"}
            ]
            },
            {"name" : "South Africa",
            "players": [
                {"name":"de kock","age":29,"role":"batsman"},
                {"name":"du plessis","age":32,"role":"batsman"},
                {"name":"rabada","age":26,"role":"bowler"},
                {"name":"ngidi","age":27,"role":"bowler"},
                {"name":"phangiso","age":34,"role":"allrounder"}
                 ]
            },
            {"name" : "Australia",
            "players": [
                {"name":"warner","age":34,"role":"batsman"},
                {"name":"finch","age":31,"role":"batsman"},
                {"name":"starc","age":30,"role":"bowler"},
                {"name":"cummins","age":28,"role":"bowler"},
                {"name":"maxwell","age":33,"role":"allrounder"}
            ]
            }
        ]
} 

#print(worldcup)
print(worldcup["country"][2]["name"])