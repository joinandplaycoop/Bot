BEGIN
	SELECT 
		Se.ServerName,
		TotalPlayersOnline,
		TotalPlayers,
		CreatedDate
	FROM
		(SELECT 
				FKServerId,
				CreatedDate,
				TotalPlayers,
				TotalPlayersOnline,
				@rn:=IF(@prev = FKServerId, @rn + 1, 1) AS rn,
				@prev:=FKServerId
		FROM
			Log
		JOIN (SELECT @prev:=NULL, @rn:=0) AS vars
		ORDER BY FKServerId , CreatedDate DESC) AS T1
		INNER JOIN Server AS Se on Se.Id = T1.FKServerId 
	WHERE
		rn <= 1
	ORDER BY Se.ServerName;    
END