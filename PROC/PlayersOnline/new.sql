BEGIN
    SELECT S.ServerName,
           Count(P.PlayerName)
    FROM   PlayersOnline
           INNER JOIN Players AS P
                   ON PlayersOnline.FKPlayerId = P.Id
           INNER JOIN Server AS S
                   ON PlayersOnline.FKServerId = S.Id
    GROUP  BY S.ServerName
    ORDER  BY S.ServerName;
END