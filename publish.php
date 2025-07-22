<?php
$data = json_decode(file_get_contents('php://input'), true);
$response = [
  "product_id" => uniqid("PROD"),
  "status" => "success",
  "title" => $data["title"]
];
header('Content-Type: application/json');
echo json_encode($response);
?>